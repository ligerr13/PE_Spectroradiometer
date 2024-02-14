from PyQt6.QtWidgets import QApplication, QMainWindow
from src.resource_1 import Ui_MainWindow
from src.navbar import NavBar
from src.nodeboard import NodeBoard
import qdarktheme



class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.navbar = NavBar(self.ui)
        self.nodeboard = NodeBoard(self.ui)

        #Calling Methods
        self.nodeboard.generateSquareTiles(self.nodeboard.grid)




    def OnNavbarButtonClicked(self, pageId: int):
        self.ui.stackedWidget.setCurrentIndex(pageId)
    





    
if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(qdarktheme.load_stylesheet("dark"))

    window = MyApp()
    window.show()
    app.exec()
