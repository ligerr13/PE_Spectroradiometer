from PyQt6.QtWidgets import QDialog, QMessageBox
from src.objects.measure_dialog import Ui_Dialog
from ..instrument.programs.basic_program import BasicProgramAndSave
from ..globals.utils import FileValidator
import asyncio, os, re

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
        
        """
        It would be awesome to select programs from a dropdown list or something.
        """
        asyncio.run(BasicProgramAndSave(file_name))
        
        self.accept()

    def cleanUp(self):
        self.ui.fileName.setText("")

    def popUp(self):
        self.cleanUp()
        self.exec()
