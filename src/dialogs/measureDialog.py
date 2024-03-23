from PyQt6.QtWidgets import QDialog
from src.objects.measure_dialog_1 import Ui_Dialog
from src.instrument.command import 
import asyncio


class MeasureDialog(QDialog):
    def __init__(self):
        super().__init__()
        
        # Setup UI
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        if self.result() == QDialog.DialogCode.Accepted:
            print("Dialog accepted")
        else:
            print("Dialog rejected")
        event.accept()

    def onAccept(self):
        print("Creating Widget")
        asyncio.run(ExecuteProgram.run_program(basic_measure_program))
        self.accept()

    def popUp(self):
        self.exec()