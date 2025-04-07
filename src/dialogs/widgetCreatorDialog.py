from PyQt6.QtWidgets import QDialog
from pathlib import Path
from src.objects.widget_creater_dialog import Ui_Dialog
from src.widgets.spectrum_widget import SpectrumWidget
from ..globals.utils import open_dialog
import json

class WidgetCreatorDialog(QDialog):
    def __init__(self):
        super().__init__()
        
        #Setup UI
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self._preview = self.ui.gridLayout_4
        self._predefined = self.ui.comboBox_4
        self._preview_widget = SpectrumWidget()
        self._preview.addWidget(self._preview_widget)

        #dimension-width
        self._width = self.ui.spinBox
        self._width_unit = self.ui.comboBox

        #dimension-height
        self._height = self.ui.spinBox_2
        self._height_unit = self.ui.comboBox_2

        #content-min-wavelength
        self._min_wavelength = self.ui.spinBox_4
        self._min_wavelength_unit = self.ui.comboBox_6

        #content-max-wavelength
        self._max_wavelength = self.ui.spinBox_5
        self._max_wavelength_unit = self.ui.comboBox_7

        #content-resolution
        self._resolution = self.ui.spinBox_6
        self._resolution_unit = self.ui.comboBox_8

        #content-select-file
        self._file_selecter_button = self.ui.pushButton
        self._selected_file_label = self.ui.label_3

        self._file_selecter_button.clicked.connect(self.open_file)
        self._width.valueChanged.connect(self.on_update_preview)
        self._height.valueChanged.connect(self.on_update_preview)
        self._min_wavelength.valueChanged.connect(self.on_update_preview)
        self._max_wavelength.valueChanged.connect(self.on_update_preview)
        self._resolution.valueChanged.connect(self.on_update_preview)

    def open_file(self) -> list[float]:
        dir = "src/instrument/data"  
        opened_file = open_dialog(self, direction=dir)

        if opened_file:
            file_path = Path(dir) / Path(opened_file)
        
            with open(file_path, 'r') as file:
                json_data = json.load(file)

                spectral_keys = [
                    "Spectral380To479JsonBuilder",
                    "Spectral480To579JsonBuilder",
                    "Spectral580To679JsonBuilder",
                    "Spectral680To780JsonBuilder"
                ]

                spectral_data = []

                for key in spectral_keys:
                    try:
                        value_str = json_data[key]["Spectral data"]["value"]
                        values = [float(v.strip()) for v in value_str.split(",")]
                        spectral_data.extend(values)
                    except (KeyError, ValueError) as e:
                        print(f"Skipping {key} due to error: {e}")


                self._preview_widget.setSpectralData(spectral_data)

                self._preview_widget.setGeometryProperties(0, 0, 300, 300)

                self._preview.addWidget(self._preview_widget)
                return spectral_data

    def reset_dialog(self):
        # Spinboxok reset
        self._width.setValue(300)
        self._height.setValue(300)
        self._min_wavelength.setValue(380)
        self._max_wavelength.setValue(780)
        self._resolution.setValue(1)

        self._width_unit.setCurrentIndex(0)
        self._height_unit.setCurrentIndex(0)
        self._min_wavelength_unit.setCurrentIndex(0)
        self._max_wavelength_unit.setCurrentIndex(0)
        self._resolution_unit.setCurrentIndex(0)

        self._selected_file_label.setText("No measurement file choosen")

        if self._preview_widget:
            self._preview.removeWidget(self._preview_widget)
            self._preview_widget.deleteLater()
        
        self._preview_widget = SpectrumWidget()
        self._preview_widget.setGeometryProperties(0, 0, 300, 300)
        self._preview.addWidget(self._preview_widget)

        self._preview.update()



    def on_update_preview(self):
        width = self._width.value()
        height = self._height.value()
        min_wl = self._min_wavelength.value()
        max_wl = self._max_wavelength.value()
        resolution = self._resolution.value()

        self._preview_widget.setGeometryProperties(0, 0, width, height)
        self._preview_widget.setWavelengthProperties(min_wl, max_wl, resolution)
        self._preview_widget.update()

    def onCustomWidgetClicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def onCustomWidget2Clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    
    def onCreateWidget(self):
        print("Creating Widget")
        self.accept()

    def onCancel(self):
        self.reset_dialog()
        self.reject()

    def popUp(self):
        self.exec()

    def closePopUp(self):
        self.reset_dialog()
        self.close()