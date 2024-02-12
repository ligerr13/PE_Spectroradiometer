from PyQt6.QtWidgets import QApplication, QMainWindow
import qdarktheme

from src.resource_1 import Ui_MainWindow
from src.navbar import NavBar

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.navbar = NavBar(self)

if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(qdarktheme.load_stylesheet("light"))

    window = MyApp()
    window.show()
    app.exec()
