from PyQt6.QtWidgets import QDialog
from src.objects.measure_dialog_1 import Ui_Dialog
from src.instrument.command import ExecuteProgram, RMTS, MSWE, MEAS, MEDR
import asyncio


basic_measure_program = [
    RMTS(switch = 1),
    MSWE(switch = 0),
    MEAS(switch = 1),
    MEDR(data_mode = 0, data_format = 0, data_block_number_to_read = 1),
  *[MEDR(data_mode=1, data_format=0, data_block_number_to_read=spectral_number) for spectral_number in range(1,5)],
    MEDR(data_mode = 2, data_format = 0, data_block_number_to_read = 0),
    RMTS(switch = 0)
]


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
        # await self.onAccept()
        self.exec()
