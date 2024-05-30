from PyQt6.QtWidgets import QApplication
from src.main import MyApp

if __name__ == "__main__":
    app = QApplication([])
    app.setStyle("Fusion")

    window = MyApp()
    window.center()
    window.show()
    app.exec()