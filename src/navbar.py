from PyQt6.QtCore import QObject
from src.dialogs.connectionConfigDialog import ConnectionConfigDialog
from src.dialogs.measureDialog2 import MeasureDialogV2

class NavBar(QObject):
    def __init__(self, resource):
        super().__init__()

        # Setup UI
        self.ui = resource

        #QDialogs
        # self.measureDialog = MeasureDialog()
        self.measureDialog = MeasureDialogV2()
        self.connectionConfigDialog = ConnectionConfigDialog()

        #Calling Methods
        
