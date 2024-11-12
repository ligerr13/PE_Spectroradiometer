from PyQt6.QtWidgets import QApplication
from src.main import MyApp
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    window = MyApp()
    window.center()
    window.show()
    app.exec()