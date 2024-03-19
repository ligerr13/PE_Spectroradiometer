from PyQt6.QtWidgets import QDialog
from src.objects.measure_dialog_1 import Ui_Dialog
from src.instrument.command import ExecuteProgram, RMTS, MSWE, MEAS, MEDR
from src.instrument.command import DataMode, DataFormat, ModeSelect, SpectralRange
import asyncio


basic_measure_program = [
    RMTS(switch = ModeSelect.ENABLED),
    MSWE(switch = ModeSelect.DISABLED),
    MEAS(switch = ModeSelect.ENABLED),
    MEDR(data_mode = DataMode.MEASUREMENT_CONDITIONS, data_format = DataFormat.ALPHANUMERIC),
    MEDR(data_mode = DataMode.SPECTRAL_DATA, data_format = DataFormat.ALPHANUMERIC, spectral_range = SpectralRange.RANGE_380_TO_479),
    MEDR(data_mode = DataMode.SPECTRAL_DATA, data_format = DataFormat.ALPHANUMERIC, spectral_range = SpectralRange.RANGE_480_TO_579),
    MEDR(data_mode = DataMode.SPECTRAL_DATA, data_format = DataFormat.ALPHANUMERIC, spectral_range = SpectralRange.RANGE_580_TO_679),
    MEDR(data_mode = DataMode.SPECTRAL_DATA, data_format = DataFormat.ALPHANUMERIC, spectral_range = SpectralRange.RANGE_680_TO_780),
    MEDR(data_mode = DataMode.COLORIMETRIC_DATA, data_format = DataFormat.ALPHANUMERIC),
    RMTS(switch = ModeSelect.DISABLED)
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
