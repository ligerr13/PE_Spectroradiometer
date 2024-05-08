from PyQt6.QtCore import QObject
from src.dialogs.measureDialog import MeasureDialog
from src.dialogs.connectionConfigDialog import ConnectionConfigDialog

class NavBar(QObject):
    def __init__(self, resource):
        super().__init__()

        # Setup UI
        self.ui = resource

        #QDialogs
        self.measureDialog = MeasureDialog()
        self.connectionConfigDialog = ConnectionConfigDialog()

        #Calling Methods
        
