from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QColor
from src.objects.workspace_landing_page_1 import Ui_Form


class WorkSpaceLandingPage(QWidget):
    newWorkspaceCreated = pyqtSignal(str)
    def __init__(self, signal_bus, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Signal Bus
        self.signal_bus = signal_bus
        
        self.ui.createWSButton.clicked.connect(self.createWS)

    def createWS(self):
        tag = self.ui.lineEdit.text()
        self.signal_bus.emitNewWorkspaceCreatedSignal(tag)