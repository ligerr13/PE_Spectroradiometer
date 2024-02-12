from PyQt6.QtWidgets import QApplication, QMainWindow

import qdarktheme

from src.resource_1 import Ui_MainWindow
from src.navbar import NavBar
from src.nodeboard import NodeBoard


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.navbar = NavBar(self.ui)   
        self.nodeboard = NodeBoard(self.ui)
        
        self.nodeboard.generateSquareTiles(self.nodeboard.grid)

if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(qdarktheme.load_stylesheet("dark"))

    window = MyApp()
    window.show()
    app.exec()
