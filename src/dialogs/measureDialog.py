from PyQt6.QtWidgets import QDialog, QMessageBox
from src.objects.measure_dialog_1 import Ui_Dialog
from src.instrument.command import ExecuteProgram, RMTS, MSWE, MEAS, MEDR
from src.instrument.command import DataMode, DataFormat, ModeSelect, SpectralRange
import asyncio, os, re


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

class FileValidator:
    @classmethod
    def get_data_directory(cls):
        script_dir = os.path.dirname(__file__)
        return os.path.abspath(os.path.join(script_dir, '..', 'instrument', 'data'))

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
            file_name = self.ui.fileName.text()
            if len(file_name) < 5:
                QMessageBox.warning(self, "Warning", "File name must be at least 5 characters long!")
                return
            elif not re.match(r'^[a-zA-Z0-9]*$', file_name):
                QMessageBox.warning(self, "Warning", "File name must contain at least one letter or number!")
                return
            elif os.path.exists(os.path.join(FileValidator.get_data_directory(), file_name + ".json")):
                QMessageBox.warning(self, "Warning", "File already exists in folder:\n" +  FileValidator.get_data_directory())
                return
            
            asyncio.run(ExecuteProgram.run_program(basic_measure_program, file_name))
            self.accept()

    def cleanUp(self):
        self.ui.fileName.setText("")

    def popUp(self):
        self.cleanUp()
        self.exec()
