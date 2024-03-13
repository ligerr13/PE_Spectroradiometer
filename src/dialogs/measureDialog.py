from PyQt6.QtWidgets import QDialog
from src.objects.measure_dialog_1 import Ui_Dialog
from src.instrument.connection import Connection

class MeasureDialog(QDialog):
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

    def onAccept(self):
        print("Start measure")
        self.accept()


    def popUp(self):
        self.exec()

    def closePopUp(self):
        self.close()