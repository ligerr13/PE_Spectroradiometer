import datetime
import logging
import os
from pathlib import Path
from PyQt6.QtCore import Qt, pyqtSignal, QTimer, QEvent
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QColor
from PyQt6.QtWidgets import QTableView, QTableWidgetItem, QDialog, QPushButton, QStyledItemDelegate
from src.instrument.examples.basic_usage import p_measure_read_store as MEASURE_PROGRAM
from src.objects.measure_dialog_prot import Ui_Dialog
from src.signals.signals import ConnectionSignals, WorkspaceSignalBus
from src.globals.utils import findAllSerialPorts
import subprocess
import sys

class ProgramLogger:
    """
    Logger for QTableView.
    """
    def __init__(self, tableView: QTableView):
        self._tableView = tableView
        self._model = QStandardItemModel()
        self._tableView.setModel(self._model)
        self._tableView.horizontalHeader().hide()
        self._tableView.verticalHeader().hide()
        self._tableView.setColumnWidth(0, 50)
        self._tableView.horizontalHeader().setStretchLastSection(True)
        self._default_color = QColor(150,200,150)
        self._resetHeaders = ['Message']
        self.idleLog()

    def addRow(self, message: str) -> QStandardItem:
        item = QStandardItem(message)
        item.setData(self._default_color, Qt.ItemDataRole.ForegroundRole)
        self._model.appendRow([item])
        self._tableView.scrollToBottom()
        return item

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
        self.generatedFiles = []
        self.generatedFileRows = []

        self._init_ui()
        self._init_signals()
        self._connect_signals()
        self._setupGeneratedFilesUI()

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

        # Just for testing 
        self.ui.pushButton_2.clicked.connect(self.runGeneratedFilesFullTest)
        # self.ui.pushButton_2.clicked.connect(self.onConnectClicked)
        self.ui.comboBox.currentIndexChanged.connect(self.onPortSelected)

    def _setupGeneratedFilesUI(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setHorizontalHeaderLabels(["File name", "", ""])
        self.ui.tableWidget.setMouseTracking(True)
        self.ui.tableWidget.viewport().installEventFilter(self)

    def popUp(self):
        self.exec()
        self.reset()

    def onConnectClicked(self):
        self.addLog("> Searching for available ports...")
        
        self.portPicker.clear()
        availablePorts = findAllSerialPorts()
        
        if not availablePorts:
            self.addLog('> Found 0 ports. Please check if the instrument is correctly connected to the device.')\
                .setData(QColor(255, 100, 103), Qt.ItemDataRole.ForegroundRole)
        else:
            self.addLog(f'> Found {len(availablePorts)} ports. Please select one.')

            for p in availablePorts:
                self.portPicker.addItem(f'{p.name} - {p.manufacturer}')


    def addLog(self, message: str):
        return self.programLogger.addRow(message)

    def resetLog(self):
        self.programLogger.clearLog()

    def onMeasurementBlocked(self):
        self.addLog("> Measurement blocked.").setData(QColor(255,100,103), Qt.ItemDataRole.ForegroundRole)

    def onPortSelected(self):
        id = self.portPicker.currentIndex()
        port = self.portPicker.itemText(id).split(" - ")[0]
        self.addLog(f"> Port {port} selected.")

    def onCalibrationStarted(self):
        self.ui.label_7.setProperty("state", "in-progress")
        self.ui.label_7.style().polish(self.ui.label_7)

    def onCalibrationEnded(self):
        self.ui.label_7.setProperty("state", "ended")
        self.ui.label_7.style().polish(self.ui.label_7)

    def onCalibrationFailed(self):
        self.ui.label_7.setProperty("state", "failed")
        self.ui.label_7.style().polish(self.ui.label_7)

    def onMeasurementStarted(self):
        self.ui.label_8.setProperty("state", "in-progress")
        self.ui.label_8.style().polish(self.ui.label_8)

    def onMeasurementEnded(self):
        self.ui.label_8.setProperty("state", "ended")
        self.ui.label_8.style().polish(self.ui.label_8)

    def onMeasurementFailed(self):
        self.ui.label_8.setProperty("state", "failed")
        self.ui.label_8.style().polish(self.ui.label_8)

    def onIdentficationFailed(self):
        self.addLog("> Instrument identification failed.").setData(QColor(255,100,103), Qt.ItemDataRole.ForegroundRole)
        self.ui.pushButton.setDisabled(True)

    def onIndentificationSuccess(self):
        self.addLog("> Instrument identified successfully.")
        self.ui.pushButton.setDisabled(False)

    def onConnectionSuccess(self):
        self.addLog("> Initialization connection...")
        self.ui.label_6.setProperty("state", "done")
        self.ui.label_6.style().polish(self.ui.label_6)

    def onConnectionFailed(self):
        self.addLog("> Initialization connection failed...").setData(QColor(255,100,103), Qt.ItemDataRole.ForegroundRole)
        self.ui.label_6.setProperty("state", "failed")
        self.ui.label_6.style().polish(self.ui.label_6)

    def onMeasureRequested(self):
        self.ui.pushButton.setDisabled(True)
        self.resetLog()
        self.addLog("> Loading measurement program...")
        self.workspace_signal_bus.emitRequestStartMeas(MEASURE_PROGRAM())

    def onAddFile(self, generated_file: str):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_4)

        self.generatedFiles.append(generated_file)

        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)

        # 0. oszlop: fájl név
        name_item = QTableWidgetItem(Path(generated_file).name)
        name_item.setFlags(name_item.flags() | Qt.ItemFlag.ItemIsEditable)
        self.ui.tableWidget.setItem(row, 0, name_item)

        # 1. oszlop: fix "Open" gomb
        btn = QPushButton("Open")
        btn.clicked.connect(lambda _, r=row: self.openGeneratedFile(r))
        self.ui.tableWidget.setCellWidget(row, 1, btn)


    def openGeneratedFile(self, row: int):
        path = self.generatedFiles[row]
        if os.path.exists(path):
            os.startfile(path)
        else:
            self.addLog(f"> File not found: {path}").setData(QColor(255,100,100), Qt.ItemDataRole.ForegroundRole)


    def eventFilter(self, source, event):
        if source is self.ui.tableWidget.viewport() and event.type() == QEvent.Type.MouseMove:
            pos = event.position().toPoint()
            row = self.ui.tableWidget.rowAt(pos.y())
            for info in self.generatedFileRows:
                info["button"].setVisible(False)
            if row >= 0:
                btn = self.ui.tableWidget.cellWidget(row, 2)
                if btn:
                    btn.setVisible(True)
        return super().eventFilter(source, event)

    def openFileExternally(self, path: str):
        if not os.path.exists(path):
            self.addLog(f"> File not found: {path}").setData(QColor(255,100,100), Qt.ItemDataRole.ForegroundRole)
            return
        if sys.platform.startswith("win"):
            os.startfile(path)
        elif sys.platform.startswith("darwin"):
            subprocess.call(["open", path])
        else:
            subprocess.call(["xdg-open", path])

    # ------------------ TEST ------------------
    def runGeneratedFilesFullTest(self):
        """
        Generates 3 dummy files and emits signals to populate tableWidget.
        """
        print("\n>>> Running GENERATED FILES TEST...")
        base_dir = Path("C:/temp/generated_test_files")
        base_dir.mkdir(parents=True, exist_ok=True)
        test_files = []
        for i in range(1,4):
            fpath = base_dir / f"measurement_test_{i}.txt"
            with open(fpath,"w") as f:
                f.write(f"Test file #{i}\nGenerated for UI auto-test.\n")
            test_files.append(str(fpath))
        for idx, fpath in enumerate(test_files):
            QTimer.singleShot(1500 + idx*800, lambda fp=fpath: self.workspace_signal_bus.measurement_file_generated.emit(fp))

    def reset(self):
        self.programLogger.idleLog()
        for lbl in [self.ui.label_6, self.ui.label_7, self.ui.label_8, self.ui.label_11]:
            lbl.setProperty("state","idle")
            lbl.style().polish(lbl)
        self.measureButton.setDisabled(False)
        self.generatedFiles.clear()
        self.generatedFileRows.clear()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
        self.ui.tableWidget.setRowCount(0)
        self.portPicker.clear()
