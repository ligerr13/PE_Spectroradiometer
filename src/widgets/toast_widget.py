import sys
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication
from PyQt6.QtCore import QTimer, Qt, QRect

from src.globals.enum import ToastType

class ToastWidget(QWidget):
    def __init__(self, message, duration=3000, toast_type = ToastType.DEFAULT, parent=None):
        super().__init__(parent)
        self.toast_type = toast_type
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.ToolTip)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        layout = QVBoxLayout(self)
        self.label = QLabel(message, self)
        self.set_style_sheet()
        layout.addWidget(self.label)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        self.adjustSize()
        
        if parent is None:
            app_instance = QApplication.instance()
            main_window = app_instance.activeWindow() if app_instance else None
            
            if main_window:
                self.setParent(main_window)
            
            screen_geometry = QApplication.primaryScreen().availableGeometry()
            self.move((screen_geometry.x() + (screen_geometry.width() - self.width())) // 4, 100)
        else:
            
            self.setParent(parent)
            
            screen_geometry = QApplication.primaryScreen().availableGeometry()
            self.move((screen_geometry.x() + (screen_geometry.width() - self.width())) // 2, 150)


        QTimer.singleShot(duration, self.close)

    def set_style_sheet(self):
        base_style = "background-color: rgb(31,31,31); padding: 10px; border-radius: 2px; font: 570 10pt 'Consolas';"
        
        if self.toast_type == ToastType.SUCCESS:
            text_color = "color: rgb(0,255,0);"
        elif self.toast_type == ToastType.ERROR:
            text_color = "color: rgb(255,0,0);"
        elif self.toast_type == ToastType.DEFAULT:
            text_color = "color: rgb(0,150,255)"
        else:
            text_color = "color: white;"
        
        style = f"{base_style} {text_color}"
        self.label.setStyleSheet(style)

    def showToast(self):
        self.show()
        self.raise_()