import serial
import platform

class Connection:
    _shared_connection = None

    @classmethod
    def get_shared_connection(cls):
        if not cls._shared_connection:
            cls._shared_connection = cls.open()
        return cls._shared_connection
    
    @staticmethod
    def open():
        try:
            port = Connection.select_port()
            if port:
                return serial.Serial(port, baudrate=9600, bytesize=8, stopbits=1, parity="N", timeout=10)
            else:
                return None
        except serial.SerialException as e:
            print("Error occurred while opening the port:", str(e))
            return None
    
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
