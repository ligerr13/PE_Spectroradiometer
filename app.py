from PyQt6.QtWidgets import QApplication
from src.main import MyApp
import traceback

if __name__ == "__main__":
    try:
        app = QApplication([])
        app.setStyle("Fusion")

        window = MyApp()
        window.center()
        window.show()

        app.exec()

    except Exception as e:
        traceback.print_exc()
