from enum import Enum
from ..widgets.toast_widget import ToastWidget
from src.globals.enum import ToastType
import os
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtCore import QObject
import numpy as np
import serial.tools.list_ports

class FileValidator:
    @classmethod
    def get_data_directory(cls):
        script_dir = os.path.dirname(__file__)
        return os.path.abspath(os.path.join(script_dir, '..', 'instrument', 'data'))
    
class Singleton(QObject):
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, *args, **kwargs):
        if self.__class__._initialized:
            return
        super().__init__()
        self.__class__._initialized = True

    
def find_serial_port(vendor_id=0x2341, product_id=0x0043):
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if port.vid == vendor_id and port.pid == product_id:
            return port.device
    
def show_toast(message, duration=3000, success=None , parent=None):
    toast = ToastWidget(message, duration, success, parent)
    toast.showToast()

def darken_color(rgb, factor=0.8):
    return tuple(int(c * factor) for c in rgb)

def open_dialog(parent, direction: str = ""):

    fname, _ = QFileDialog.getOpenFileName(
                parent,
                "Open File",
                f"{direction}",
                "JSON Files (*.json)",
        )
        
    file_name = os.path.basename(fname)

    return file_name

def open_folder_dialog(parent, direction: str = ""):
    folder = QFileDialog.getExistingDirectory(
        parent,
        "Select Folder",
        directory=direction
    )
    return folder

def convert_numpy(obj):
    """ Ha az objektum egy ndarray, listává alakítja """
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")
