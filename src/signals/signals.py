from types import CoroutineType
from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QGraphicsProxyWidget, QWidget
from src.widgets.scene_widget import SceneWidget

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

    add_widget_to_current_workspace = pyqtSignal(QGraphicsProxyWidget)

    fileNameUpdated = pyqtSignal(str)

    request_start_measurement = pyqtSignal(object)
    request_cancel_measurement = pyqtSignal()

    def __init__(self):
        super().__init__()

    def emitRequestStartMeas(self, program):
        self.request_start_measurement.emit(program)
    
    def emitRequestCancelMeas(self):
        self.request_cancel_measurement.emit()

    def emitCloseWorkspaceSignal(self):
        self.closeWorkspace.emit()

    def emitFileNameUpdatedSignal(self, file_name: str):
        self.fileNameUpdated.emit(file_name)

    def emitNewWorkspaceCreatedSignal(self, tag):
        self.newWorkspaceCreated.emit(tag)

    def emitWidgetDataToPorpertyEditor(self, property_holder):
        self.widgetDataToPorpertyEditor.emit(property_holder)

    def emitUpdateExplorer(self):
        self.update_explorer.emit()

    def emitUpdateOptions(self, key: str, row: int):
        self.update_options.emit(key, row)

    def emitAddWidgetToCurrentWorkspace(self, widget: QGraphicsProxyWidget):
        self.add_widget_to_current_workspace.emit(widget)
