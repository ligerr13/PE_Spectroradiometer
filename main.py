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
        if drag is not None:
            if  drag == False:
                self.nodeboard.view.setDragMode(QGraphicsView.DragMode.NoDrag)
                self.sender().setStyleSheet("QPushButton {border: 0px;}QPushButton:hover {background: rgb(55, 55, 55);}")
            else:
                self.nodeboard.view.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
                self.sender().setStyleSheet("QPushButton {border: 0px;background-color: rgb(63, 101, 255);}, QPushButton:hover {background: rgb(55, 55, 55);}")

    def HandleSelectMode(self, select: bool):
        if select is not None:
            if  select == False:
                self.sender().setStyleSheet("QPushButton {border: 0px;}QPushButton:hover {background: rgb(55, 55, 55);}")
            else:
                self.sender().setStyleSheet("QPushButton {border: 0px;background-color: rgb(63, 101, 255);}, QPushButton:hover {background: rgb(55, 55, 55);}")

    def OnNavbarButtonClicked(self, pageId: int):
        self.ui.stackedWidget.setCurrentIndex(pageId)


if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(qdarktheme.load_stylesheet("dark"))

    window = MyApp()
    window.show()
    app.exec()
