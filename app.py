from PyQt6.QtWidgets import QApplication
from src.main import MyApp

import asyncio
import traceback
from qasync import QEventLoop

import logging
from pathlib import Path

Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,  # vagy INFO, ha sok a részlet
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("logs/instrument.log", encoding="utf-8"),
        logging.StreamHandler()  # terminálra is ír
    ]
)

if __name__ == "__main__":
    try:
        app = QApplication([])
        app.setStyle("Fusion")

        loop = QEventLoop(app)
        asyncio.set_event_loop(loop)

        window = MyApp()
        window.center()
        window.show()

        with loop:
            try:
                loop.run_forever()
            finally:
                pending = asyncio.Task.all_tasks()
                group = asyncio.gather(*pending, return_exceptions=True)

                loop.run_until_complete(group)
                loop.close()

                print('All tasks concluded.')

    except Exception as e:
        traceback.print_exc()
