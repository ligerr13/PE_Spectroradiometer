from PyQt6.QtWidgets import QWidget
from PyQt6 import QtCore

class SceneWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, objectName = "SpectralData Widget")

    @property
    def objectName(self):
        return self.property("objectName")
    
    @objectName.setter
    def objectName(self, value):
       self.setObjectName(value)

    @property
    def minimumWidth(self):
        return self.property("minimumWidth")

    @minimumWidth.setter
    def minimumWidth(self, value):
        self.setMinimumWidth(value)

    @property
    def minimumHeight(self):
        return self.property("minimumHeight")

    @minimumHeight.setter
    def minimumHeight(self, value):
        self.setMinimumHeight(value)

    @property
    def maximumWidth(self):
        return self.property("maximumWidth")

    @maximumWidth.setter
    def maximumWidth(self, value):
        self.setMaximumWidth(value)

    @property
    def maximumHeight(self):
        return self.property("maximumHeight")

    @maximumHeight.setter
    def maximumHeight(self, value):
        self.setMaximumHeight(value)

    @property
    def width(self):
        return self.property("width")

    @width.setter
    def width(self, width, height):
        self.resize(width , height)

    @property
    def height(self):
        return self.property("height")

    @height.setter
    def height(self, width, height):
        self.resize(width, height)

    @property
    def x(self):
        return self.property("x")

    @x.setter
    def x(self, value):
        self.move(value, self.y)

    @property
    def y(self):
        return self.property("y")

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