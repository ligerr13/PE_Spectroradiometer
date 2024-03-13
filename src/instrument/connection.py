import serial
import platform

class Connection:
    def __init__(self):
        self.serial_port = None

    def select_port(self):
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

    def open(self):
        try:
            port = self.select_port()
            if port:
                self.serial_port = serial.Serial(port, baudrate=9600, bytesize=8, stopbits=1, parity="N", timeout=10)
                return True
            else:
                return False
        except serial.SerialException as e:
            print("Error occurred while opening the port:", str(e))
            return False

    def close(self):
        if self.serial_port:
            self.serial_port.close()
            self.serial_port = None
            
# python -m serial.tools.list_ports 