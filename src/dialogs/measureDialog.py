# import logging
# import time
# from PyQt6.QtWidgets import QDialog
# from PyQt6.QtCore import pyqtSignal, Qt
# from src.objects.measure_dialog import Ui_Dialog
# from src.signals.signals import WorkspaceSignalBus
# from src.instrument.examples.basic_usage import p_measure_read_store


# class MeasureDialog(QDialog):
#     def __init__(self):
#         super().__init__()

#         self.ui = Ui_Dialog()
#         self.ui.setupUi(self)

#         self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
#         self.workspace_signal_bus = WorkspaceSignalBus.instance()

#         self.workspace_signal_bus.measurement_started.connect(self.on_measurement_started)
#         # self.workspace_signal_bus.measurement_ended.connect(self.on_measurement_ended)
#         self.workspace_signal_bus.measurement_canceled.connect(self.on_measurement_canceled)
#         # self.workspace_signal_bus.measurement_blocked.connect(self.on_measurement_blocked)

#     def on_measurement_started(self):
#         logging.info("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

#     # def on_measurement_ended(self):
#     #     logging.info("MeasureDialog: Measurement ended (completed or failed).")
#     #     self._update_ui_for_idle_state()

#     def on_measurement_canceled(self):
#         logging.info("MeasureDialog: Measurement cancelled.")
#         self.ui.start_stop_button.setChecked(False)

#     # def on_measurement_blocked(self):
#     #     logging.warning("MeasureDialog: Measurement blocked. Resetting UI.")
#     #     self._update_ui_for_idle_state() 

#     def onAccept(self, checked: bool):
#         if not checked: # Button is checked (start measurement state)
#             logging.debug("Measure button checked. Requesting start measurement.")
#             self.ui.start_stop_button.setText("Requesting...")
#             self.ui.start_stop_button.setEnabled(False)

#             time.sleep(0.25)

#             self.workspace_signal_bus.emitRequestStartMeas(p_measure_read_store())

#         else:
#             logging.debug("Measure button unchecked. Requesting cancel measurement.")
#             self.ui.start_stop_button.setText("Cancelling...")
#             self.ui.start_stop_button.setEnabled(False)
#             self.workspace_signal_bus.emitRequestCancelMeas()

#     def cleanUp(self):
#         logging.debug("MeasureDialog cleanup performed.")

#     def popUp(self):
#         self.cleanUp()
#         self.exec()
