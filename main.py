from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView
from PyQt6.QtGui import QTransform

from src.objects.resource_1 import Ui_MainWindow
from src.navbar import NavBar
from src.nodeboard import NodeBoard

import qdarktheme



class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        #Setup UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #QObject
        self.nodeboard = NodeBoard(self.ui)
        self.navbar = NavBar(self.ui)
        

        #Calling Methods
        self.nodeboard.generateSquareTiles(self.nodeboard.grid)
                             
        #Temporary
        self.ui.pushButton_10.setChecked(True)


    #MainWindow Slots
    def HandleDragMode(self, drag: bool):        
        if drag is not None:
            if  drag == False:
                self.nodeboard.view.setDragMode(QGraphicsView.DragMode.NoDrag)
            else:
                self.nodeboard.view.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)

    def HandleSelectMode(self, select: bool):
        try:
            if select is not None:
                if select == False:
                    self.nodeboard.scene.setSelecteButton(None)
                else:
                    self.nodeboard.scene.setSelecteButton(self.sender())
        except AttributeError as e:
            print("An AttributeError occurred:", e)


    def HandleDeleteMode(self, delete: bool):
        if delete is not None:
            if  delete == False:
                self.nodeboard.scene.setDeleteButton(None)
            else:
                self.nodeboard.scene.setDeleteButton(self.sender())

    def HandleCreateWidgetMode(self, create: bool):
        if create is not None:
            if  create == False:
                # self.nodeboard.scene.setDeleteButton(None)
                self.nodeboard.widgetCreator.closePopUp()
            else:
                # self.nodeboard.scene.setDeleteButton(self.sender())
                self.nodeboard.widgetCreator.popUp()

    def OnNavbarButtonClicked(self, pageId: int):
        self.ui.stackedWidget.setCurrentIndex(pageId)


    def HandleZoomIn(self):
        scale_tr = QTransform()
        scale_tr.scale(self.nodeboard.viewScalefactor, self.nodeboard.viewScalefactor)

        tr = self.nodeboard.view.transform() * scale_tr
        if tr.m11() <= 2.0 and tr.m22() <= 2.0:
            self.nodeboard.view.setTransform(tr)

    def HandleZoomOut(self):
        scale_tr = QTransform()
        scale_tr.scale(1 / self.nodeboard.viewScalefactor, 1 / self.nodeboard.viewScalefactor)

        tr = self.nodeboard.view.transform() * scale_tr
        if tr.m11() >= 0.4 and tr.m22() >= 0.4:
            self.nodeboard.view.setTransform(tr)

if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(qdarktheme.load_stylesheet("dark"))

    window = MyApp()
    window.show()
    app.exec()
