import serial, platform, json
from PyQt6.QtWidgets import QMessageBox

class Connection:
    _shared_connection = None
    
    @classmethod
    def get_shared_connection(cls):
        if not cls._shared_connection:
            cls._shared_connection = cls.open()
        return cls._shared_connection
    
    @staticmethod
    def load_serial_settings():
        try:
            with open("instrument/config/connection_config.json", "r") as file:
                return json.load(file)
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error loading JSON connection config file 'connection_config.json': {e}")
            return None
        
            
    @staticmethod
    def open():
        try:
            port = Connection.select_port()
            if port:
                port_settings = Connection.load_serial_settings()
                if port_settings:
                    return serial.Serial(port, **port_settings)
                else:
                    print("Failed to load serial settings.")
            else:
                print("Port is not available.")
        except serial.SerialException as e:
            print("Error occurred while opening the port:", str(e))

    @staticmethod
    def select_port():
        try:
            if platform.system() == "Darwin":
                return '/dev/cu.usbmodem12345678901'
            elif platform.system() == "Windows":
                return 'COM3'
            else:
                print("Unsupported platform:", platform.system())
                return None
        except Exception as e:
            print("Error occurred while selecting the port:", str(e))
            return None

    @staticmethod
    def close(serial_port):
        if serial_port:
            serial_port.close()
            Connection._shared_connection = None
