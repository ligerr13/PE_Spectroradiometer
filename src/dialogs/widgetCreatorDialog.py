from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QDialog, QAbstractButton
from pathlib import Path
# from src.objects.widget_creater_dialog import Ui_Dialog
from src.objects.widget_creator_new import Ui_Dialog
from src.widgets.spectrum_widget import SpectrumWidget
from src.widgets.locus_widget import LocusWidget, LocusConfig
from ..globals.utils import open_dialog
import json
from src.signals.signals import WorkspaceSignalBus


class WidgetCreatorDialog(QDialog):

    should_reset = pyqtSignal()
    should_update_preview = pyqtSignal(int)
    current_page_id: int = 0

    def __init__(self, parent=None):
        super().__init__(parent)
        
        #Setup UI
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.signal_bus =  WorkspaceSignalBus.instance()

        self._selected_file: str
        self.should_reset.connect(self.onResetDialog)
        self.should_update_preview.connect(self.onUpdatePreview)

        self.current_widget = None
        self._spectral_data = []
        self._colorimetric_data = {}

        self._spectral_preview_widget = SpectrumWidget()
        self._spectral_preview = self.ui.gridLayout_7
        self._spectral_preview.addWidget(self._spectral_preview_widget)


        self._locus_preview_widget = LocusWidget()
        self._locus_preview = self.ui.gridLayout_8
        self._locus_preview.addWidget(self._locus_preview_widget)

        self.current_page_id = 0
        self.setPages(0)
        self.current_widget = self._spectral_preview_widget
    
    def HandlePages(self, button):
        name = button.objectName()

        if name == "spectrum_colors_btn":
            self.current_page_id = 0
            self.current_widget = self._spectral_preview_widget
        elif name == "spectrum_locus_btn":
            self.current_page_id = 1
            self.current_widget = self._locus_preview_widget


        self.setPages(self.current_page_id)

    def ImportData(self):
        dir = "src/instrument/data"
        opened_file = open_dialog(self, direction=dir)

        if opened_file:
            file_path = Path(dir) / Path(opened_file)

            try:
                with open(file_path, 'r') as file:
                    json_data = json.load(file)
                    
                    spectral_data = []
                    colorimetric_data = {}

                    spectral_keys = ["Spectral380To479JsonBuilder","Spectral480To579JsonBuilder","Spectral580To679JsonBuilder","Spectral680To780JsonBuilder"]

                    for key in spectral_keys:
                        try:
                            value_str = json_data[key]["Spectral data"]["value"]
                            values = [float(v.strip()) for v in value_str.split(",")]
                            spectral_data.extend(values)
                        except (KeyError, ValueError) as e:
                            print(f"Skipping {key} due to error: {e}")

                    self._spectral_data = spectral_data

                    try:
                        colorimetric_section = json_data["ColorimetricJsonBuilder"]["Colorimetric Data"]
                        for key, entry in colorimetric_section.items():
                            colorimetric_data[key] = float(entry["value"].replace(" ", ""))
                    except (KeyError, ValueError) as e:
                        print(f"Error parsing colorimetric data: {e}")

                    self._colorimetric_data = colorimetric_data

            except Exception as e:
                print(f"Unknown error: {e}")

            self.ui.choosen_file_label.setText(str(file_path))
            self._selected_file = file_path
            self.should_update_preview.emit(self.current_page_id)

    def onUpdatePreview(self, current_page_id: int):
        match current_page_id:
            case 0:
                width = self.ui.spinBox_7.value()
                height = self.ui.spinBox_8.value()

                min_wl = self.ui.spinBox_4.value()
                max_wl = self.ui.spinBox_5.value()

                self._spectral_preview_widget.setGeometryProperties(0, 0, width, height)
                self._spectral_preview_widget.configure(self._spectral_data, min_wl, max_wl)
            case 1:
                width = self.ui.spinBox_13.value()
                height = self.ui.spinBox_12.value()

                cctext = self.ui.checkBox_11.isChecked()
                eew = self.ui.checkBox_10.isChecked()
                dl = self.ui.checkBox_9.isChecked()
                bbl = self.ui.checkBox_8.isChecked()
                d65 = self.ui.checkBox_6.isChecked()

                self._locus_preview_widget.setGeometryProperties(0, 0, width, height)
                self._locus_preview_widget.configure(self._colorimetric_data,cctext, eew, dl, bbl, d65)

            case _:
                pass

    def onCreateWidget(self):
        if self.current_widget:
            self.signal_bus.add_widget_to_current_workspace.emit(self.current_widget)
        self.accept()

    def onResetDialog(self):
        self._selected_file = ""
        self.ui.choosen_file_label.clear()
        self.current_page_id = 0

    def onCancel(self):
        self.should_reset.emit()
        self.reject()

    def popUp(self):
        self.exec()

    def closePopUp(self):
        self.should_reset.emit()
        self.close()

    def setPages(self, page_id) -> None:
        self.ui.stacked_contents.setCurrentIndex(page_id)
        self.ui.stacked_dimensions.setCurrentIndex(page_id)
        self.ui.stacked_previews.setCurrentIndex(page_id)
