from PyQt6.QtWidgets import QDialog, QMessageBox
from src.objects.measure_dialog_1 import Ui_Dialog
from src.instrument.command import ExecuteProgram, RMTS, MSWE, MEAS, MEDR
from src.instrument.command import DataMode, DataFormat, ModeSelect, SpectralRange
import asyncio, os, re


class MeasureProgramBuilder:
    def __init__(self):
        self.measure_program = []        

    def enable_spectral_data(self):
        self.measure_program.append(MEDR(data_mode=SpectralRange.RANGE_380_TO_479, data_format=DataFormat.ALPHANUMERIC))
        self.measure_program.append(MEDR(data_mode=SpectralRange.RANGE_480_TO_579, data_format=DataFormat.ALPHANUMERIC))
        self.measure_program.append(MEDR(data_mode=SpectralRange.RANGE_580_TO_679, data_format=DataFormat.ALPHANUMERIC))
        self.measure_program.append(MEDR(data_mode=SpectralRange.RANGE_680_TO_780, data_format=DataFormat.ALPHANUMERIC))

    def enable_colorimetric_data(self):
        self.measure_program.append(MEDR(data_mode=DataMode.COLORIMETRIC_DATA, data_format=DataFormat.ALPHANUMERIC))

    def enable_measurement_conditions(self):
        self.measure_program.append(MEDR(data_mode=DataMode.MEASUREMENT_CONDITIONS, data_format=DataFormat.ALPHANUMERIC))

    def build(self):
        self.measure_program.insert(0, RMTS(switch=ModeSelect.ENABLED))
        self.measure_program.insert(1, MEAS(switch=ModeSelect.ENABLED))
        self.measure_program.append(RMTS(switch=ModeSelect.DISABLED))
        return self.measure_program

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

        self.measurement_conditions_checkBox = self.ui.checkBox
        self.spectral_data_checkBox = self.ui.checkBox_2
        self.colorimetric_data_checkBox = self.ui.checkBox_3

        self.timer = self.ui.spinBox
        self.times = self.ui.doubleSpinBox

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
        
        measure_program_builder = MeasureProgramBuilder()
        if self.measurement_conditions_checkBox.isChecked():
            measure_program_builder.enable_measurement_conditions()
        if self.spectral_data_checkBox.isChecked():
            measure_program_builder.enable_spectral_data()
        if self.colorimetric_data_checkBox.isChecked():
            measure_program_builder.enable_colorimetric_data()
        
        measure_program = measure_program_builder.build()

        asyncio.run(ExecuteProgram.run_program(measure_program, file_name))
        self.accept()

    def cleanUp(self):
        self.ui.fileName.setText("")

    def popUp(self):
        self.cleanUp()
        self.exec()
