from PyQt6.QtWidgets import QDialog, QMessageBox, QLineEdit
from src.objects.connection_info import Ui_Dialog
from PyQt6.QtCore import pyqtSignal
import json
from src.globals.enum import ToastType

class ConnectionConfigDialog(QDialog):
    serial_settings_has_changed = pyqtSignal(ToastType, str)
    
    def __init__(self):
        super().__init__()
        
        # Setup UI
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Connect signals to slots
        self.ui.buttonBox.accepted.connect(self.onAccept)
        self.ui.buttonBox.rejected.connect(self.closePopUp)
    
    @staticmethod
    def load_serial_settings():
        try:
            with open("src/instrument/config/connection_config.json", "r") as file:
                return json.load(file)
        except Exception as e:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Critical)
            msg_box.setText(f"Error loading JSON connection config file 'connection_config.json': {e}")
            msg_box.setWindowTitle("Error")
            msg_box.exec()
            return None
        
    def update_serial_settings(self):
        try:
            data = ConnectionConfigDialog.load_serial_settings()
            if data is None:
                return
            
            data["baudrate"] = int(self.ui.baudrateQLineEdit.text())
            data["port"] = str(self.ui.lineEdit.text())
            data["bytesize"] = int(self.ui.bytesizeQLineEdit.text())
            data["stopbits"] = int(self.ui.stopbitQLineEdit.text())
            data["parity"] = str(self.ui.parityQLineEdit.text())
            data["timeout"] = int(self.ui.timeoutQLineEdit.text())

            with open("src/instrument/config/connection_config.json", "w") as file:
                json.dump(data, file, indent=4)

            self.serial_settings_has_changed.emit(ToastType.SUCCESS, "Connection settings have been updated successfully.")
                
        except Exception as e:
            self.serial_settings_has_changed.emit(ToastType.ERROR, "Unable to process the connection configuration file due to an error.")
            return None
        
    def closeEvent(self, event):
        if self.result() == QDialog.DialogCode.Accepted:
            print("Dialog accepted")
        else:
            print("Dialog rejected")
        event.accept()

    def onAccept(self):
        self.update_serial_settings()
        self.accept()

    def popUp(self) -> bool:
        try:
            data = ConnectionConfigDialog.load_serial_settings()
            if data is None:
                return

            self.ui.baudrateQLineEdit.setText(str(data["baudrate"]))
            self.ui.lineEdit.setText(str(data["port"]))
            self.ui.bytesizeQLineEdit.setText(str(data["bytesize"]))
            self.ui.stopbitQLineEdit.setText(str(data["stopbits"]))
            self.ui.parityQLineEdit.setText(str(data["parity"]))
            self.ui.timeoutQLineEdit.setText(str(data["timeout"]))

        except FileNotFoundError:
            print("The specified JSON file cannot be found.")
        except json.JSONDecodeError:
            print("An error occurred while decoding the JSON file.")        
        
        self.exec()

    def closePopUp(self):
        self.close()
