from PyQt6.QtGui import QMouseEvent
from PyQt6 import QtGui
from PyQt6.QtWidgets import QWidget
from PyQt6 import QtCore
from PyQt6.QtCore import pyqtSignal, Qt, QPointF

from .serializable_widget import SerializableWidget

class SceneWidget(SerializableWidget):
    enableMovementSignal = pyqtSignal(bool)

    def __init__(self, parent=None):
        super().__init__(widget_id="SpectralData Widget", widget_type="SceneWidget", data=None)
        self.setObjectName("SpectralData Widget")
        self.oldPos = None
        self.moveable = False
        self.enableMovementSignal.connect(self.enable_movement)
    
    def enable_movement(self, value: bool = True):
        self.moveable = value
        if self.moveable:
            self.setCursor(QtGui.QCursor(Qt.CursorShape.CrossCursor))
        else:
            self.setCursor(QtGui.QCursor(Qt.CursorShape.ArrowCursor)) 
    
    def mousePressEvent(self, evt: QMouseEvent):
        if not self.moveable: return
        
        self.oldPos = evt.globalPosition()
        evt.accept()

    def mouseMoveEvent(self, evt: QMouseEvent):
        if self.oldPos is None: return 
        if not self.moveable: return

        delta = QPointF(evt.globalPosition() - self.oldPos)
        
        self.move(int(self.x + delta.x()), int(self.y + delta.y()))
        
        self.oldPos = evt.globalPosition()
        evt.accept()

    def mouseReleaseEvent(self, evt: QMouseEvent):
        self.oldPos = None
        evt.accept()

    @property
    def objectName(self):
        return super().objectName()

    @objectName.setter
    def objectName(self, value):
        self.setObjectName(value)

    @property
    def minimumWidth(self):
        return super().minimumWidth()

    @minimumWidth.setter
    def minimumWidth(self, value):
        self.setMinimumWidth(value)

    @property
    def minimumHeight(self):
        return super().minimumHeight()

    @minimumHeight.setter
    def minimumHeight(self, value):
        self.setMinimumHeight(value)

    @property
    def maximumWidth(self):
        return super().maximumWidth()

    @maximumWidth.setter
    def maximumWidth(self, value):
        self.setMaximumWidth(value)

    @property
    def maximumHeight(self):
        return super().maximumHeight()

    @maximumHeight.setter
    def maximumHeight(self, value):
        self.setMaximumHeight(value)

    @property
    def width(self):
        return self.geometry().width()

    @width.setter
    def width(self, value):
        self.resize(value, self.height)

    @property
    def height(self):
        return self.geometry().height()

    @height.setter
    def height(self, value):
        self.resize(self.width, value)

    @property
    def x(self):
        return self.geometry().x()

    @x.setter
    def x(self, value):
        self.move(value, self.y)

    @property
    def y(self):
        return self.geometry().y()

    @y.setter
    def y(self, value):
        self.move(self.x, value)

    @property
    def stylesheet(self):
        return self.styleSheet()

    @stylesheet.setter
    def stylesheet(self, value):
        self.setStyleSheet(value)

    def setGeometryProperties(self, x, y, width, height):
        self.setGeometry(QtCore.QRect(x, y, width, height))