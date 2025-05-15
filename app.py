from PyQt6.QtWidgets import QApplication
from src.main import MyApp

import asyncio
import traceback
from qasync import QEventLoop

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
                loop.close()

    except Exception as e:
        traceback.print_exc()
