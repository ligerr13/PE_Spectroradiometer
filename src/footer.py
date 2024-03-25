from PyQt6.QtCore import QObject
from src.dialogs.connectionConfigDialog import ConnectionConfigDialog

class Footer(QObject):
    def __init__(self, resource):
        super().__init__()

        # Setup UI
        self.ui = resource
        self.connection_toolbutton = self.ui.toolButton_2

        #QDialogs
        self.connectionConfigDialog = ConnectionConfigDialog()