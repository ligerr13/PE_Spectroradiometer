from PyQt6.QtWidgets import QDialog
from PyQt6.QtCore import pyqtSignal, Qt
from src.objects.measure_dialog import Ui_Dialog
from src.signals.signals import WorkspaceSignalBus
from src.instrument.examples.basic_usage import p_measure_read_store


class MeasureDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.workspace_signal_bus = WorkspaceSignalBus.instance()

    def onAccept(self, option):
        if option == False:
           self.workspace_signal_bus.emitRequestStartMeas(p_measure_read_store)
        # else:
        #    self.workspace_signal_bus.emitRequestCancelMeas()

    def cleanUp(self):
        pass

    def popUp(self):
        self.cleanUp()
        self.exec()