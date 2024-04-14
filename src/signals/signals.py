from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtWidgets import QGraphicsProxyWidget

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
    closeWorkspace = pyqtSignal()

    def __init__(self):
        super().__init__()

    def emitCloseWorkspaceSignal(self):
        print("Signal emited")
        self.closeWorkspace.emit()