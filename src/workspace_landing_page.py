from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QColor
from src.objects.workspace_landing_page import Ui_Form
from src.signals.signals import WorkspaceSignalBus



class WorkSpaceLandingPage(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Signal Bus
        self.signal_bus =  WorkspaceSignalBus.instance()

        
        # Signals
        self.ui.createWSButton.clicked.connect(self.createWS)

        # Actions
        self.addAction(self.ui.actioncreate_on_enter)
        self.ui.actioncreate_on_enter.triggered.connect(lambda: self.createWS())

    def createWS(self):
        tag = self.ui.lineEdit.text()
        self.signal_bus.emitNewWorkspaceCreatedSignal(tag)