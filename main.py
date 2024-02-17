from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QAbstractButton
from src.objects.resource_1 import Ui_MainWindow
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



    #MainWindow Slots
    def HandleDragMode(self, drag: bool):
        print(self.sender(), drag)
        
        if drag is not None:
            if  drag == False:
                self.nodeboard.view.setDragMode(QGraphicsView.DragMode.NoDrag)
            else:
                self.nodeboard.view.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)

    def OnNodeboardSceneButtonClicked(self, Button):
        if Button == self.nodeboard.prev_button:
            self.nodeboard.prev_button.setStyleSheet("QPushButton {border: 0px;}QPushButton:hover {background: rgb(55, 55, 55);}")
            self.nodeboard.prev_button = None
        else:
            if self.nodeboard.prev_button is not None:
                self.nodeboard.prev_button.setStyleSheet("QPushButton {border: 0px;}QPushButton:hover {background: rgb(55, 55, 55);}")
            Button.setStyleSheet("QPushButton {border: 0px;background-color: rgb(63, 101, 255);}, QPushButton:hover {background: rgb(55, 55, 55);}")
            self.nodeboard.prev_button = Button        
        
    def OnNavbarButtonClicked(self, pageId: int):
        self.ui.stackedWidget.setCurrentIndex(pageId)


if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(qdarktheme.load_stylesheet("dark"))

    window = MyApp()
    window.show()
    app.exec()
