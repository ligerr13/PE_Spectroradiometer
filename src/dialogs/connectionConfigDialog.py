from PyQt6.QtWidgets import QDialog
from src.objects.connection_info_1 import Ui_Dialog

class ConnectionConfigDialog(QDialog):
    def __init__(self):
        super().__init__()
        
        #Setup UI
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        #Calling Methods
    
    def closeEvent(self, event):
            if self.result() == QDialog.DialogCode.Accepted:
                print("Dialog accepted")
            else:
                print("Dialog rejected")
            event.accept()

    def onAccept(self):
        self.accept()

    def popUp(self):
        self.exec()

    def closePopUp(self):
        self.close()