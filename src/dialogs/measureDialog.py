from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtCore import pyqtSignal, Qt
from src.objects.measure_dialog import Ui_Dialog
from ..instrument.examples.basic_usage import run_program, _measure_read_store, error_handler
from ..globals.utils import FileValidator, open_folder_dialog
from pathlib import Path
import asyncio, os, re



class MeasureDialog(QDialog):
    check_compatibility = pyqtSignal()


    def __init__(self):
        super().__init__()
        
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Setup UI
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.save_path_button = self.ui.pushButton
        self.save_path_label = self.ui.label_3
        self.save_path = ''

        # self.measurement_conditions_checkBox = self.ui.checkBox
        # self.spectral_data_checkBox = self.ui.checkBox_2
        # self.colorimetric_data_checkBox = self.ui.checkBox_3

        # self.timer = self.ui.spinBox
        # self.times = self.ui.doubleSpinBox

        self.check_compatibility.connect(self.onCheckName)
        self.save_path_button.clicked.connect(self.onCheckFolder)

    def closeEvent(self, event):
        event.accept()

    def onCheckFolder(self):
        dir = "src/instrument/data"  
        folder = open_folder_dialog(self, direction=dir)
        
        if folder:
            self.save_path = Path(folder)
            self.save_path_label.setText(str(self.save_path))

    def onAccept(self):
        if self.onCheckName():
            file_name = self.ui.fileName.text().strip()
            full_path = self.save_path / f"{file_name}.json"
            print(f"Saving to: {full_path}")
            run_program(_measure_read_store, error_handler)
            self.accept()

    def onCheckName(self):
        file_name = self.ui.fileName.text().strip()

        if len(file_name) < 5:
            QMessageBox.warning(self, "Warning", "File name must be at least 5 characters long!")
            return False
        elif not re.match(r'^[a-zA-Z0-9_-]+$', file_name):
            QMessageBox.warning(self, "Warning", "File name can only contain letters, numbers, underscores or hyphens.")
            return False
        elif not self.save_path:
            QMessageBox.warning(self, "Warning", "Please select a save location first.")
            return False
        elif (self.save_path / f"{file_name}.json").exists():
            QMessageBox.warning(self, "Warning", f"File already exists in folder:\n{self.save_path}")
            return False
        
        return True


    def cleanUp(self):
        # self.save_path_label.clear()
        pass

    def popUp(self):
        self.cleanUp()
        self.exec()
