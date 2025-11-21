from datetime import datetime
from serial.tools import list_ports
from enum import Enum
from ..widgets.toast_widget import ToastWidget
from src.globals.enum import ToastType
import os
from PyQt6.QtWidgets import QFileDialog, QTreeWidgetItem
from PyQt6.QtCore import QObject, Qt
import numpy as np
import serial.tools.list_ports
from pathlib import Path

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

    
def find_serial_port(vendor_id, product_id):
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
    fnames, _ = QFileDialog.getOpenFileNames(
        parent,
        "Open File",
        direction,
        "JSON Files (*.json)",
    )

    return [Path(f) for f in fnames]

def open_folder_dialog(parent, direction: str = ""):
    folder = QFileDialog.getExistingDirectory(
        parent,
        "Select Folder",
        directory=direction
    )
    return folder

def convert_numpy(obj):
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

def findAllSerialPorts():
    return list_ports.comports()

def is_valid_measurement_file(data: dict) -> bool:
    try:
        if "MeasurementJsonBuilder" not in data:
            return False
        if "Measurement Conditions" not in data["MeasurementJsonBuilder"]:
            return False

        if "ColorimetricJsonBuilder" not in data:
            return False
        if "Colorimetric Data" not in data["ColorimetricJsonBuilder"]:
            return False

        spectral_keys = [
            "Spectral380To479JsonBuilder",
            "Spectral480To579JsonBuilder",
            "Spectral580To679JsonBuilder",
            "Spectral680To780JsonBuilder",
        ]

        for key in spectral_keys:
            if key not in data:
                return False
            if "Spectral data" not in data[key]:
                return False

        return True

    except Exception:
        return False

def get_file_date(path):
    timestamp = os.path.getmtime(path)
    return datetime.fromtimestamp(timestamp)

def add_file_to_tree(tree, filepath, file_date):
    """
    file_date: datetime objektum
    """

    date_key = file_date.strftime("%Y-%m-%d")

    category_item = None
    for i in range(tree.topLevelItemCount()):
        item = tree.topLevelItem(i)
        if item.text(0) == date_key:
            category_item = item
            break

    if category_item is None:
        category_item = QTreeWidgetItem([date_key])
        category_item.setExpanded(True)
        tree.addTopLevelItem(category_item)

    filename = filepath.name

    file_item = QTreeWidgetItem([filename])
    file_item.setCheckState(0, Qt.CheckState.Unchecked)

    category_item.addChild(file_item)
