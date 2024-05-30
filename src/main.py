from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QMenu
from PyQt6.QtGui import QGuiApplication, QKeySequence
from PyQt6.QtCore import  QCoreApplication, QPoint

from src.objects.resource import Ui_MainWindow
from src.navbar import NavBar
from src.tab_manager import TabManager
from src.workspace_template import Workspace
from src.signals.signals import WorkspaceSignalBus
from src.workspace_landing_page import WorkSpaceLandingPage
from src.objects.fileContextMenu import Ui_Form

class FileContextMenu(QMenu):
    def __init__(self):
        super().__init__()
        self.file_context_menu = Ui_Form()
        self.file_context_menu.setupUi(self)

        ## Submenu
        ## Like edit

        ## Display and add actions to FileContextMenu
        self.addAction(self.file_context_menu.actionHome_Page)
        self.addAction(self.file_context_menu.actionNew_Workspace)
        self.addAction(self.file_context_menu.actionSave)
        self.addAction(self.file_context_menu.actionSave_All)
        self.addAction(self.file_context_menu.actionClose_Workspace)
        self.addAction(self.file_context_menu.actionClose_All_Workspace)
        self.addAction(self.file_context_menu.actionClose_Window)

        ## Separators
        self.insertSeparator(self.file_context_menu.actionClose_Workspace)
        self.insertSeparator(self.file_context_menu.actionNew_Workspace)
        self.insertSeparator(self.file_context_menu.actionSave)

        ## Calling Methods 
        self.file_context_menu.actionClose_Window.setShortcut(QKeySequence("Ctrl+Q"))

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        ## Setup UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.navbar = NavBar(self.ui)
        self.tm = TabManager(self.ui)
        self.fcu = FileContextMenu()

        ## Actions
        self.addActions([
            self.fcu.file_context_menu.actionHome_Page,
            self.fcu.file_context_menu.actionNew_Workspace,
            self.fcu.file_context_menu.actionSave,
            self.fcu.file_context_menu.actionSave_All,
            self.fcu.file_context_menu.actionClose_Workspace,
            self.fcu.file_context_menu.actionClose_All_Workspace,
            self.fcu.file_context_menu.actionClose_Window
        ])

        ## Signal Bus
        self.signal_bus = WorkspaceSignalBus()

        ## Signals
        self.tm.file_menu_button.clicked.connect(self.handle_file_context_menu)
        self.tm.plusClicked.connect(lambda: self.tm.add_page(WorkSpaceLandingPage(self.signal_bus), "New Workspace"))
        self.fcu.file_context_menu.actionNew_Workspace.triggered.connect(lambda: self.tm.add_page(WorkSpaceLandingPage(self.signal_bus), "New Workspace"))
        self.fcu.file_context_menu.actionClose_Window.triggered.connect(lambda: QCoreApplication.quit()) ##TODO: Call handler check unsaved ws and then quit. 
        self.fcu.file_context_menu.actionClose_Workspace.triggered.connect(lambda: self.tm.remove_page(self.tm.get_current_page_index())) ##TODO: Call handler check unsaved ws and then quit.
        self.signal_bus.newWorkspaceCreated.connect(self.handleNewWorkspaceCreation)



        ##Calling Methods
        self.tm.add_page(Workspace(self.signal_bus), "Test Workspace")
    
    def handle_file_context_menu(self):
        sender_button = self.sender()
        global_pos = sender_button.mapToGlobal(sender_button.pos())
        global_pos += QPoint(-5, 32)
        self.fcu.exec(global_pos)
        self.tm.file_menu_button.clearFocus()

    def handleNewWorkspaceCreation(self, tag):
        self.tm.remove_page(self.tm.get_current_page_index())
        self.tm.add_page(Workspace(self.signal_bus), tag)

    def HandleMeasureDialog(self, selected: bool):
        if selected is not None:
            self.navbar.measureDialog.popUp()
            self.sender().setChecked(False)

    def HandleConnectionConfigDialog(self):
        self.navbar.connectionConfigDialog.popUp()

    def center(self):
        qr = self.frameGeometry()           
        cp = QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())