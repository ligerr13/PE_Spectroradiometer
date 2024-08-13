from enum import Enum
from ..widgets.toast_widget import ToastWidget

def show_toast(message, duration=3000, success=None , parent=None):
    toast = ToastWidget(message, duration, success, parent)
    toast.showToast()
