from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView
from PyQt6.QtGui import QTransform

from src.objects.resource_1 import Ui_MainWindow
from src.navbar import NavBar
from src.tabmanager import TabManager
from src.workspaceTemplate import WorkspaceDesignWidget
from src.signals.signals import WorkspaceSignalBus

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        #Setup UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.navbar = NavBar(self.ui)
        self.tm = TabManager(self.ui)


        #Signals
        signal_bus = WorkspaceSignalBus()


        #QObject
        

        #Calling Methods
        self.tm.setup_connections(signal_bus)
        stuff_to_pickle = WorkspaceDesignWidget(signal_bus)

        self.tm.add_page(stuff_to_pickle, "Test_Workspace    ")
        # self.tm.save_page_to_file(stuff_to_pickle, "Test_Workspace")

        self.tm.add_page(WorkspaceDesignWidget(signal_bus), "Test_Workspace2    ")
        
        # #Temporary
        self.ui.pushButton_13.setChecked(True)


    #MainWindow Slots
    def HandleMeasureDialog(self, selected: bool):
        if selected is not None:
            # if selected == False:
            #     self.navbar.measureDialog.closePopUp()
            # else:
                self.navbar.measureDialog.popUp()
                self.sender().setChecked(False)

    def HandleConnectionConfigDialog(self):
        self.navbar.connectionConfigDialog.popUp()

    def OnNavbarButtonClicked(self, pageId: int):
        # self.ui.stackedWidget.setCurrentIndex(pageId)
        pass



if __name__ == "__main__":
    app = QApplication([])
    app.setStyle("Fusion")

    window = MyApp()
    window.show()
    app.exec()
