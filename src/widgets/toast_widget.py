from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication
from PyQt6.QtCore import QTimer, Qt, QRect, QPropertyAnimation, QEasingCurve, QPoint
from PyQt6.QtGui import QPixmap
from src.objects.toast_widget import Ui_Form
from src.globals.enum import ToastType

class ToastWidget(QWidget):
    def __init__(self, message, duration=1000, toast_type=ToastType.DEFAULT, parent=None):
        super().__init__(parent)
        self.toast_type = toast_type
        self.message = message
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.ToastMessage.setText(self.message)
        self.adjust_size_to_text()
        self.set_style_sheet()

        self.setParent(parent)
        self.start_pos = QPoint(parent.width() // 2 - self.width() // 2, parent.height())
        self.end_pos = QPoint(parent.width() // 2 - self.width() // 2, 65)
        
        self.start_animation()

        QTimer.singleShot(duration, self.close)

    def start_animation(self):
        """Animate the widget's movement and opacity."""
        self.animation = QPropertyAnimation(self, b"pos")
        self.animation.setDuration(1000)
        self.animation.setStartValue(self.start_pos)
        self.animation.setEndValue(self.end_pos)
        self.animation.setEasingCurve(QEasingCurve.Type.OutBounce)
        self.animation.start()

    def set_style_sheet(self):
        """Set the stylesheet based on the toast type."""
        if self.toast_type == ToastType.SUCCESS:
            background_color = "rgb(1,175,110)"
            icon_background_color = "rgb(0,140,88)"
            text_color = "white"
            toast_icon_path = "resources/icons/double-check.png"
        elif self.toast_type == ToastType.ERROR:
            background_color = "rgb(220,82,56)"
            icon_background_color = "rgb(173,65,44)"
            text_color = "white"
            toast_icon_path = "resources/icons/sign.png"
        elif self.toast_type == ToastType.DEFAULT:
            background_color = "rgb(0,150,255)"
            icon_background_color = "rgba(0,150,255,0.8)"
            text_color = "white"
        else:
            background_color = "white"
            icon_background_color = "rgba(255,255,255,0.8)"
            text_color = "black"

        widget_style = f"background-color: {background_color}; padding: 10px; border-radius: 2px;"
        icon_widget_style = f"background: {icon_background_color}; margin 10 10 10 10;"
        label_style = f"color: {text_color}; font: 570 10pt 'Consolas';"

        self.ui.widget_4.setStyleSheet(icon_widget_style)
        self.ui.ToastMessage.setStyleSheet(label_style)
        self.setStyleSheet(widget_style)

        pixmap = QPixmap(toast_icon_path)
        self.ui.ToastIcon.setPixmap(pixmap)

    def adjust_size_to_text(self):
        """Adjust the widget size based on message length, up to a certain limit."""
        max_chars_per_line = 50
        char_width = 7
        padding = 20

        text_length = len(self.message)
        if text_length >= max_chars_per_line:
            width = max_chars_per_line * char_width + padding
            self.ui.ToastMessage.setFixedWidth(width)

        self.ui.ToastMessage.setWordWrap(True)

    def showToast(self):
        self.show()
        self.raise_()
