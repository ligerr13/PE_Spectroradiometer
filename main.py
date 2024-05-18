from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView
from PyQt6.QtGui import QTransform, QGuiApplication


from src.objects.resource_1 import Ui_MainWindow
from src.navbar import NavBar
from src.tab_manager import TabManager
from src.workspace_template import Workspace
from src.signals.signals import WorkspaceSignalBus
from src.workspace_landing_page import WorkSpaceLandingPage

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        #Setup UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.navbar = NavBar(self.ui)
        self.tm = TabManager(self.ui)

        #Signals
        self.signal_bus = WorkspaceSignalBus()

        # Connect the plusClicked signal to add_page method
        self.tm.plusClicked.connect(lambda: self.tm.add_page(WorkSpaceLandingPage(self.signal_bus), "New Workspace"))
        
        self.workspace_page = WorkSpaceLandingPage(self.signal_bus)
        self.signal_bus.newWorkspaceCreated.connect(self.handleNewWorkspaceCreation)

    def handleNewWorkspaceCreation(self, tag):
        self.tm.remove_page(self.tm.get_current_page_index())
        self.tm.add_page(Workspace(self.signal_bus), tag)

    #MainWindow Slots
    def HandleMeasureDialog(self, selected: bool):
        if selected is not None:
            self.navbar.measureDialog.popUp()
            self.sender().setChecked(False)

    def HandleConnectionConfigDialog(self):
        self.navbar.connectionConfigDialog.popUp()

    def OnNavbarButtonClicked(self, pageId: int):
        # self.ui.stackedWidget.setCurrentIndex(pageId)
        pass

    def center(self):
        qr = self.frameGeometry()           
        cp = QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())




if __name__ == "__main__":
    app = QApplication([])
    app.setStyle("Fusion")

    window = MyApp()
    window.center()
    window.show()
    app.exec()
