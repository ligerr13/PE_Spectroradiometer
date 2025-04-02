from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QGraphicsProxyWidget, QWidget

class NodeBoardSignalBus(QObject):
    widgetSelectedSignal = pyqtSignal(QGraphicsProxyWidget)
    widgetDeselectedSignal = pyqtSignal(QGraphicsProxyWidget)
    widgetDeletedSignal = pyqtSignal(QGraphicsProxyWidget)

    def __init__(self):
        super().__init__()

    def onWidgetSelectedSignalEmit(self, widget):
        self.widgetSelectedSignal.emit(widget)

    def onWidgetDeselectedSignalEmit(self, widget):
        self.widgetDeselectedSignal.emit(widget)

    def onWidgetDeletedSignalEmit(self, widget):
        self.widgetDeletedSignal.emit(widget)

class WorkspaceSignalBus(QObject):
    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    closeWorkspace = pyqtSignal()
    newWorkspaceCreated = pyqtSignal(str)

    widgetDataToPorpertyEditor = pyqtSignal(QWidget)

    update_explorer = pyqtSignal()

    update_options = pyqtSignal(str, int)

    

    def __init__(self):
        super().__init__()

    def emitCloseWorkspaceSignal(self):
        self.closeWorkspace.emit()

    def emitNewWorkspaceCreatedSignal(self, tag):
        self.newWorkspaceCreated.emit(tag)

    def emitWidgetDataToPorpertyEditor(self, property_holder):
        self.widgetDataToPorpertyEditor.emit(property_holder)

    def emitUpdateExplorer(self):
        self.update_explorer.emit()

    def emitUpdateOptions(self, key: str, row: int):
        self.update_options.emit(key, row)