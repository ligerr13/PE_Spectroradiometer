from PyQt6.QtCore import  QSize, pyqtSignal, QObject, QPoint, Qt
from PyQt6.QtWidgets import QTabBar, QPushButton, QMenu, QMenuBar, QTreeWidgetItem
from PyQt6.QtGui import QIcon, QKeySequence
from PyQt6 import QtCore

from enum import Enum



class WorkscapeExplorer(QObject):
    _instance = None
    _explorer = None
    
    class WidgetType(Enum):
        WIDGET = "Widget"
        TEXT = "Text"
        IMAGE = "Image"
        OTHER = "Other"

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @property
    def explorer(self):
        return self._explorer

    @explorer.setter
    def explorer(self, explorer):
        self._explorer = explorer

    def add_one(self, row: WidgetType, item: QTreeWidgetItem):
        widget_items = self.explorer.findItems(row.value, Qt.MatchFlag.MatchExactly | Qt.MatchFlag.MatchRecursive)
        if widget_items:
            widget_items[0].addChild(item)

    def remove_one(self, row: WidgetType, item: QTreeWidgetItem):
        widget_items = self.explorer.findItems(row.value, Qt.MatchFlag.MatchExactly | Qt.MatchFlag.MatchRecursive)
        if widget_items:
            widget_items[0].removeChild(item)
    
    def remove_many(self):
        pass

    def remove_all(self):
        pass