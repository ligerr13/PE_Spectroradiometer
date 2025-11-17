import datetime
import logging
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QColor
from PyQt6.QtWidgets import QTableView, QDialog
from src.instrument.examples.basic_usage import p_measure_read_store as MEASURE_PROGRAM
from src.objects.measure_dialog_prot import Ui_Dialog
from src.signals.signals import ConnectionSignals, WorkspaceSignalBus
from src.globals.utils import findAllSerialPorts
class ProgramLogger:
    def __init__(self, tableView: QTableView):
        self._headers = ['Time', 'Message']
        self._resetHeaders = ['Message']

        self._tableView = tableView
        self._model = QStandardItemModel()
        
        self._default_color = QColor(150, 200, 150)
        self._how_to_color = QColor(150, 150, 150)

        self._model.setHorizontalHeaderLabels(self._resetHeaders)
        self._tableView.setModel(self._model)
        self._tableView.setColumnWidth(0, 50)
        self._tableView.horizontalHeader().setStretchLastSection(True)
        self._tableView.horizontalHeader().hide()
        self._tableView.verticalHeader().hide()

        self.idleLog()
        

    def addRow(self, message: str) -> QStandardItem:
        message_item = QStandardItem(message)
        color = self._default_color
        message_item.setData(color, Qt.ItemDataRole.ForegroundRole)
        self._model.appendRow([message_item])
        self._tableView.scrollToBottom()
        
        return message_item

    def clearLog(self):
        self._model.clear()

    def idleLog(self):
        self.clearLog()
        self._model.setHorizontalHeaderLabels(self._resetHeaders)
        self.addRow("Waiting for measurement to start...").setData(QColor(150,150,150), Qt.ItemDataRole.ForegroundRole)

class MeasureDialogV2(QDialog):
    refershSteps = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._init_ui()
        self._init_signals()
        self._connect_signals()

    def _init_ui(self):
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.measureButton = self.ui.pushButton
        self.programLogger = ProgramLogger(self.ui.tableView)
        self.portPicker = self.ui.comboBox

        self.ui.label_6.setProperty("state", "idle")
        self.ui.label_7.setProperty("state", "idle")
        self.ui.label_8.setProperty("state", "idle")
        self.ui.label_11.setProperty("state", "idle")

    def _init_signals(self):
        self.connection_signals = ConnectionSignals.instance() 
        self.workspace_signal_bus = WorkspaceSignalBus.instance()

    def _connect_signals(self):
        self.measureButton.pressed.connect(self.onMeasureRequested)
        self.connection_signals.success.connect(self.onConnectionSuccess)
        self.connection_signals.failed.connect(self.onConnectionFailed)
        self.workspace_signal_bus.measurement_blocked.connect(self.onMeasurementBlocked)
        self.workspace_signal_bus.calibration_started.connect(self.onCalibrationStarted)
        self.workspace_signal_bus.calibration_ended.connect(self.onCalibrationEnded)
        self.workspace_signal_bus.calibration_failed.connect(self.onCalibrationFailed)
        self.workspace_signal_bus.measurement_started.connect(self.onMeasurementStarted)
        self.workspace_signal_bus.measurement_ended.connect(self.onMeasurementEnded)
        self.workspace_signal_bus.measurement_failed.connect(self.onMeasurementFailed)
        self.workspace_signal_bus.identification_failed.connect(self.onIdentficationFailed)
        self.workspace_signal_bus.identification_success.connect(self.onIndentificationSuccess)
        self.workspace_signal_bus.measurement_file_generated.connect(self.onAddFile)

        self.ui.pushButton_2.clicked.connect(self.onConnectClicked)
        self.ui.comboBox.currentIndexChanged.connect(self.onPortSelected)

    def popUp(self):
        self.exec()
        self.reset()

    def onIdentficationFailed(self):
        self.addLog("> Instrument identification failed. Please check the connection and try again.").setData(QColor(255, 100, 103), Qt.ItemDataRole.ForegroundRole)
        self.ui.pushButton.setDisabled(True)

    def onIndentificationSuccess(self):
        self.addLog("> Instrument identified successfully.")
        self.ui.pushButton.setDisabled(False)
    
    def onPortSelected(self):
        id = self.ui.comboBox.currentIndex()
        port = self.ui.comboBox.itemText(id).split(' - ')[0]
        self.addLog(f'> Port {port} selected.')


    def onConnectClicked(self):
        self.addLog("> Searching for available ports...")
        
        self.portPicker.clear()
        availablePorts = findAllSerialPorts()
        
        if not availablePorts:
            self.addLog(f'> Found 0 ports. Please check if the instrument is correctly connected to the device.').setData(QColor(255, 100, 103), Qt.ItemDataRole.ForegroundRole)
        else:
            self.addLog(f'> Found {len(availablePorts)} ports. Please select one.')

            for p in availablePorts:
                self.portPicker.addItem(f'{p.name} - {p.manufacturer}')

    def onMeasurementStarted(self):
        logging.info("Measurement about to start..")
        self.ui.label_6.setProperty("state", "in-progress")
        self.ui.label_6.style().polish(self.ui.label_6)

    def onMeasureRequested(self):
        self.ui.pushButton.setDisabled(True)
        self.resetLog()
        self.addLog("> Loading measurement program...")
        self.workspace_signal_bus.emitRequestStartMeas(MEASURE_PROGRAM())

    def onIdleEntered(self):
        print("Idle state entered, should set the things")

    def addLog(self, message: str) -> QStandardItem:
        result = self.programLogger.addRow(message)
        return result
    
    def resetLog(self):
        self.programLogger.clearLog()

    def onConnectionSuccess(self):
        self.addLog("> Initialization connection...")
        self.ui.label_6.setProperty("state", "done")
        self.ui.label_6.style().polish(self.ui.label_6)
        
    def onConnectionFailed(self):
        self.addLog("> Initialization connection failed...").setData(QColor(255, 100, 103), Qt.ItemDataRole.ForegroundRole)
        self.ui.label_6.setProperty("state", "failed")
        self.ui.label_6.style().polish(self.ui.label_6)

    def onMeasurementBlocked(self):
        pass

    # Calibration State
    def onCalibrationStarted(self):
        self.ui.label_7.setProperty("state", "in-progress")
        self.ui.label_7.style().polish(self.ui.label_7)

    def onCalibrationEnded(self):
        self.ui.label_7.setProperty("state", "ended")
        self.ui.label_7.style().polish(self.ui.label_7)

    def onCalibrationFailed(self):
        self.ui.label_7.setProperty("state", "failed")
        self.ui.label_7.style().polish(self.ui.label_7)

    # Measurement State
    def onMeasurementStarted(self):
        self.ui.label_8.setProperty("state", "in-progress")
        self.ui.label_8.style().polish(self.ui.label_8)

    def onMeasurementEnded(self):
        self.ui.label_8.setProperty("state", "ended")
        self.ui.label_8.style().polish(self.ui.label_8)
    
    def onMeasurementFailed(self):
        self.ui.label_8.setProperty("state", "failed")
        self.ui.label_8.style().polish(self.ui.label_8)

    def onAddFile(generated_file: str):
        print(generated_file)

    def reset(self):
        self.programLogger.idleLog()

        for lbl in [self.ui.label_6, self.ui.label_7, self.ui.label_8, self.ui.label_11]:
            lbl.setProperty("state", "idle")
            lbl.style().polish(lbl)

        self.measureButton.setDisabled(False)
        self.portPicker.clear()

    def closeEvent(self, event):
        if self.ui.label_8.property("state") == "in-progress":
            self.addLog("> Cannot close dialog: measurement in progress.")
            event.ignore()
            return

        self.reset()
        super().closeEvent(event)


