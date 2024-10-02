import os

from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QMenu, QFileDialog
from PyQt6.QtGui import QGuiApplication, QKeySequence
from PyQt6.QtCore import  QCoreApplication, QPoint, pyqtSlot

from src.objects.resource import Ui_MainWindow
from src.navbar import NavBar
from src.tab_manager import TabManager
from src.workspace_template import Workspace
from src.signals.signals import WorkspaceSignalBus
from src.workspace_landing_page import WorkSpaceLandingPage
from src.objects.fileContextMenu import Ui_Form
from src.globals.utils import show_toast, ToastType

class FileContextMenu(QMenu):
    def __init__(self):
        super().__init__()
        self.file_context_menu = Ui_Form()
        self.file_context_menu.setupUi(self)

        ## Display and add actions to FileContextMenu
        self.addAction(self.file_context_menu.actionHome_Page)
        self.addAction(self.file_context_menu.actionNew_Workspace)
        self.addAction(self.file_context_menu.actionSaveAs)
        self.addAction(self.file_context_menu.actionSave_All)
        self.addAction(self.file_context_menu.actionopen_workspace_form_file)
        self.addAction(self.file_context_menu.actionClose_Workspace)
        self.addAction(self.file_context_menu.actionClose_All_Workspace)
        self.addAction(self.file_context_menu.actionClose_Window)

        ## Separators
        self.insertSeparator(self.file_context_menu.actionClose_Workspace)
        self.insertSeparator(self.file_context_menu.actionNew_Workspace)
        self.insertSeparator(self.file_context_menu.actionSaveAs)

        ## Calling Methods 
        self.file_context_menu.actionClose_Window.setShortcut(QKeySequence("Ctrl+Q"))
        self.file_context_menu.actionHome_Page.setShortcut(QKeySequence("Ctrl+H"))

from PyQt6.QtWidgets import QMainWindow, QMessageBox
from src.globals.utils import show_toast

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setup UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.navbar = NavBar(self.ui)
        self.tm = TabManager(self.ui)
        self.fcu = FileContextMenu()

        # Actions
        self.addActions([
            self.fcu.file_context_menu.actionHome_Page,
            self.fcu.file_context_menu.actionNew_Workspace,
            self.fcu.file_context_menu.actionSaveAs,
            self.fcu.file_context_menu.actionSave_All,
            self.fcu.file_context_menu.actionClose_Workspace,
            self.fcu.file_context_menu.actionClose_All_Workspace,
            self.fcu.file_context_menu.actionClose_Window
        ])

        # Signal Bus
        self.signal_bus = WorkspaceSignalBus.instance()

        # Signals
        self.tm.file_menu_button.clicked.connect(self.handle_file_context_menu)
        self.tm.plusClicked.connect(lambda: self.tm.add_page(WorkSpaceLandingPage(), "New Workspace"))
        self.fcu.file_context_menu.actionNew_Workspace.triggered.connect(lambda: self.tm.add_page(WorkSpaceLandingPage(), "New Workspace"))
        self.fcu.file_context_menu.actionClose_Window.triggered.connect(lambda: QCoreApplication.quit())
        self.fcu.file_context_menu.actionClose_Workspace.triggered.connect(lambda: self.tm.remove_page(self.tm.get_current_page_index()))
        self.fcu.file_context_menu.actionHome_Page.triggered.connect(lambda: self.tm.tabWidget.setCurrentIndex(self.tm.get_page_by_tabname("home")))
        
        self.navbar.connectionConfigDialog.serial_settings_has_changed.connect(self.onUpdateSerialSettings)

        self.fcu.file_context_menu.actionopen_workspace_form_file.triggered.connect(self.open_dialog_and_create_workspace)
        self.fcu.file_context_menu.actionSaveAs.triggered.connect(self.save_current_workspace)
        self.signal_bus.newWorkspaceCreated.connect(self.handleNewWorkspaceCreation)

        # Calling Methods
        self.tm.add_page(Workspace("Default", self), "Default")

    @pyqtSlot()
    def open_dialog_and_create_workspace(self):
        fname, _ = QFileDialog.getOpenFileName(
                self,
                "Open File",
                "",
                "JSON Files (*.json)",
        )
        
        file_name = os.path.basename(fname)
        if not fname: 
            show_toast("No file selected.", 3000, ToastType.ERROR, self)
            return

        self.new_page(file_name)
        show_toast(f"Opened workspace: {file_name}", 3000, ToastType.SUCCESS, self)
            
    @pyqtSlot()
    def save_current_workspace(self):
        fname, _ = QFileDialog.getSaveFileName(
                self,
                "Save Workspace",
                "",
                "JSON Files (*.json)"
        )

        if not fname: 
            show_toast("No file selected for saving.", 3000, ToastType.ERROR, self) 
            return

        if not fname.endswith('.json'):
            fname += '.json'

        file_name = os.path.basename(fname)
        wk_id = self.tm.get_current_page_widget()
        if not wk_id: 
            show_toast("No workspace to save.", 3000, ToastType.ERROR, self)
            return

        wk_id.save_workspace(file_name)
        show_toast(f"Saved workspace: {file_name}", 3000, ToastType.SUCCESS, self)

    def handle_file_context_menu(self):
        sender_button = self.sender()
        global_pos = sender_button.mapToGlobal(sender_button.pos())
        global_pos += QPoint(-5, 46)
        self.fcu.exec(global_pos)
        self.tm.file_menu_button.clearFocus()

    def handleNewWorkspaceCreation(self, tag):
        self.tm.remove_page(self.tm.get_current_page_index())
        self.tm.add_page(Workspace(tag, self), tag)
        show_toast(f"Created new workspace: {tag}", 3000, ToastType.SUCCESS, self)

    def new_page(self, tag):
        wk = Workspace(tag, self)
        self.tm.add_page(wk, tag)
        wk.load_workspace(tag, self)

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

    def onUpdateSerialSettings(self, state: ToastType, message: str):
        show_toast(f"Connection: {message}", 3000, state, self)
