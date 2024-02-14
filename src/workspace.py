from PyQt6.QtCore import QObject, QLineF
from PyQt6.QtWidgets import QGraphicsScene
from PyQt6.QtGui import QColor, qRgb


class WorkSpace(QObject):
    def __init__(self, resource):
        super().__init__()
        self.ui = resource

        self.prev_button = None

        #Signals and Connections
        # self.ui.pushButton_7
        # self.ui.pushButton_8
        # self.ui.pushButton_9
