from enum import Enum
from ..widgets.toast_widget import ToastWidget
from src.globals.enum import ToastType
import os
from PyQt6.QtWidgets import QFileDialog

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

    print(file_name)