from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import QPoint, Qt
from PyQt6.QtGui import QMouseEvent
from PyQt6 import QtGui
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib import cm
from .scene_widget import SceneWidget
from luxpy import plot_spectrum_colors ,spd, vlbar_cie_mesopic, spectrum, cri_ref
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class SpectrumWidget(SceneWidget):
    wavelength = np.array([3.8000e+02, 3.8100e+02, 3.8200e+02, 3.8300e+02, 3.8400e+02,
    3.8500e+02, 3.8600e+02, 3.8700e+02, 3.8800e+02, 3.8900e+02,
    3.9000e+02, 3.9100e+02, 3.9200e+02, 3.9300e+02, 3.9400e+02,
    3.9500e+02, 3.9600e+02, 3.9700e+02, 3.9800e+02, 3.9900e+02,
    4.0000e+02, 4.0100e+02, 4.0200e+02, 4.0300e+02, 4.0400e+02,
    4.0500e+02, 4.0600e+02, 4.0700e+02, 4.0800e+02, 4.0900e+02,
    4.1000e+02, 4.1100e+02, 4.1200e+02, 4.1300e+02, 4.1400e+02,
    4.1500e+02, 4.1600e+02, 4.1700e+02, 4.1800e+02, 4.1900e+02,
    4.2000e+02, 4.2100e+02, 4.2200e+02, 4.2300e+02, 4.2400e+02,
    4.2500e+02, 4.2600e+02, 4.2700e+02, 4.2800e+02, 4.2900e+02,
    4.3000e+02, 4.3100e+02, 4.3200e+02, 4.3300e+02, 4.3400e+02,
    4.3500e+02, 4.3600e+02, 4.3700e+02, 4.3800e+02, 4.3900e+02,
    4.4000e+02, 4.4100e+02, 4.4200e+02, 4.4300e+02, 4.4400e+02,
    4.4500e+02, 4.4600e+02, 4.4700e+02, 4.4800e+02, 4.4900e+02,
    4.5000e+02, 4.5100e+02, 4.5200e+02, 4.5300e+02, 4.5400e+02,
    4.5500e+02, 4.5600e+02, 4.5700e+02, 4.5800e+02, 4.5900e+02,
    4.6000e+02, 4.6100e+02, 4.6200e+02, 4.6300e+02, 4.6400e+02,
    4.6500e+02, 4.6600e+02, 4.6700e+02, 4.6800e+02, 4.6900e+02,
    4.7000e+02, 4.7100e+02, 4.7200e+02, 4.7300e+02, 4.7400e+02,
    4.7500e+02, 4.7600e+02, 4.7700e+02, 4.7800e+02, 4.7900e+02,
    4.8000e+02, 4.8100e+02, 4.8200e+02, 4.8300e+02, 4.8400e+02,
    4.8500e+02, 4.8600e+02, 4.8700e+02, 4.8800e+02, 4.8900e+02,
    4.9000e+02, 4.9100e+02, 4.9200e+02, 4.9300e+02, 4.9400e+02,
    4.9500e+02, 4.9600e+02, 4.9700e+02, 4.9800e+02, 4.9900e+02,
    5.0000e+02, 5.0100e+02, 5.0200e+02, 5.0300e+02, 5.0400e+02,
    5.0500e+02, 5.0600e+02, 5.0700e+02, 5.0800e+02, 5.0900e+02,
    5.1000e+02, 5.1100e+02, 5.1200e+02, 5.1300e+02, 5.1400e+02,
    5.1500e+02, 5.1600e+02, 5.1700e+02, 5.1800e+02, 5.1900e+02,
    5.2000e+02, 5.2100e+02, 5.2200e+02, 5.2300e+02, 5.2400e+02,
    5.2500e+02, 5.2600e+02, 5.2700e+02, 5.2800e+02, 5.2900e+02,
    5.3000e+02, 5.3100e+02, 5.3200e+02, 5.3300e+02, 5.3400e+02,
    5.3500e+02, 5.3600e+02, 5.3700e+02, 5.3800e+02, 5.3900e+02,
    5.4000e+02, 5.4100e+02, 5.4200e+02, 5.4300e+02, 5.4400e+02,
    5.4500e+02, 5.4600e+02, 5.4700e+02, 5.4800e+02, 5.4900e+02,
    5.5000e+02, 5.5100e+02, 5.5200e+02, 5.5300e+02, 5.5400e+02,
    5.5500e+02, 5.5600e+02, 5.5700e+02, 5.5800e+02, 5.5900e+02,
    5.6000e+02, 5.6100e+02, 5.6200e+02, 5.6300e+02, 5.6400e+02,
    5.6500e+02, 5.6600e+02, 5.6700e+02, 5.6800e+02, 5.6900e+02,
    5.7000e+02, 5.7100e+02, 5.7200e+02, 5.7300e+02, 5.7400e+02,
    5.7500e+02, 5.7600e+02, 5.7700e+02, 5.7800e+02, 5.7900e+02,
    5.8000e+02, 5.8100e+02, 5.8200e+02, 5.8300e+02, 5.8400e+02,
    5.8500e+02, 5.8600e+02, 5.8700e+02, 5.8800e+02, 5.8900e+02,
    5.9000e+02, 5.9100e+02, 5.9200e+02, 5.9300e+02, 5.9400e+02,
    5.9500e+02, 5.9600e+02, 5.9700e+02, 5.9800e+02, 5.9900e+02,
    6.0000e+02, 6.0100e+02, 6.0200e+02, 6.0300e+02, 6.0400e+02,
    6.0500e+02, 6.0600e+02, 6.0700e+02, 6.0800e+02, 6.0900e+02,
    6.1000e+02, 6.1100e+02, 6.1200e+02, 6.1300e+02, 6.1400e+02,
    6.1500e+02, 6.1600e+02, 6.1700e+02, 6.1800e+02, 6.1900e+02,
    6.2000e+02, 6.2100e+02, 6.2200e+02, 6.2300e+02, 6.2400e+02,
    6.2500e+02, 6.2600e+02, 6.2700e+02, 6.2800e+02, 6.2900e+02,
    6.3000e+02, 6.3100e+02, 6.3200e+02, 6.3300e+02, 6.3400e+02,
    6.3500e+02, 6.3600e+02, 6.3700e+02, 6.3800e+02, 6.3900e+02,
    6.4000e+02, 6.4100e+02, 6.4200e+02, 6.4300e+02, 6.4400e+02,
    6.4500e+02, 6.4600e+02, 6.4700e+02, 6.4800e+02, 6.4900e+02,
    6.5000e+02, 6.5100e+02, 6.5200e+02, 6.5300e+02, 6.5400e+02,
    6.5500e+02, 6.5600e+02, 6.5700e+02, 6.5800e+02, 6.5900e+02,
    6.6000e+02, 6.6100e+02, 6.6200e+02, 6.6300e+02, 6.6400e+02,
    6.6500e+02, 6.6600e+02, 6.6700e+02, 6.6800e+02, 6.6900e+02,
    6.7000e+02, 6.7100e+02, 6.7200e+02, 6.7300e+02, 6.7400e+02,
    6.7500e+02, 6.7600e+02, 6.7700e+02, 6.7800e+02, 6.7900e+02,
    6.8000e+02, 6.8100e+02, 6.8200e+02, 6.8300e+02, 6.8400e+02,
    6.8500e+02, 6.8600e+02, 6.8700e+02, 6.8800e+02, 6.8900e+02,
    6.9000e+02, 6.9100e+02, 6.9200e+02, 6.9300e+02, 6.9400e+02,
    6.9500e+02, 6.9600e+02, 6.9700e+02, 6.9800e+02, 6.9900e+02,
    7.0000e+02, 7.0100e+02, 7.0200e+02, 7.0300e+02, 7.0400e+02,
    7.0500e+02, 7.0600e+02, 7.0700e+02, 7.0800e+02, 7.0900e+02,
    7.1000e+02, 7.1100e+02, 7.1200e+02, 7.1300e+02, 7.1400e+02,
    7.1500e+02, 7.1600e+02, 7.1700e+02, 7.1800e+02, 7.1900e+02,
    7.2000e+02, 7.2100e+02, 7.2200e+02, 7.2300e+02, 7.2400e+02,
    7.2500e+02, 7.2600e+02, 7.2700e+02, 7.2800e+02, 7.2900e+02,
    7.3000e+02, 7.3100e+02, 7.3200e+02, 7.3300e+02, 7.3400e+02,
    7.3500e+02, 7.3600e+02, 7.3700e+02, 7.3800e+02, 7.3900e+02,
    7.4000e+02, 7.4100e+02, 7.4200e+02, 7.4300e+02, 7.4400e+02,
    7.4500e+02, 7.4600e+02, 7.4700e+02, 7.4800e+02, 7.4900e+02,
    7.5000e+02, 7.5100e+02, 7.5200e+02, 7.5300e+02, 7.5400e+02,
    7.5500e+02, 7.5600e+02, 7.5700e+02, 7.5800e+02, 7.5900e+02,
    7.6000e+02, 7.6100e+02, 7.6200e+02, 7.6300e+02, 7.6400e+02,
    7.6500e+02, 7.6600e+02, 7.6700e+02, 7.6800e+02, 7.6900e+02,
    7.7000e+02, 7.7100e+02, 7.7200e+02, 7.7300e+02, 7.7400e+02,
    7.7500e+02, 7.7600e+02, 7.7700e+02, 7.7800e+02, 7.7900e+02,
    7.8000e+02])
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.data = None
        self.plt = plt
        self.sub_type = "Spectrum-Color"
        self.plt.style.use("seaborn-v0_8")

        self.min_wavelength = 0
        self.max_wavelength = 0

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.pc = MplCanvas(self)
        layout.addWidget(self.pc)

        self.toolbar = NavigationToolbar(self.pc, self)
        layout.addWidget(self.toolbar)

    def get_widget_data(self):
        super().get_widget_data()
        geometry = self.geometry()
        return {
            'id': self.widget_id,
            'type': self.widget_type,
            'sub-type': self.sub_type,
            'uniqe_name': self.objectName,
            'geometry': {
                'x': geometry.x(),
                'y': geometry.y(),
                'width': geometry.width(),
                'height': geometry.height()
            },
            'range': {
                'min': self.min_wavelength, 
                'max':self.max_wavelength
            }, 
            'data': self.data
        }

    def configure(self, data, min_wl, max_wl):
        self.data = data
        self.min_wavelength = min_wl
        self.max_wavelength = max_wl
        self.plot_data()

    def plot_data(self):
        if self.data is None:
            return

        mask = (SpectrumWidget.wavelength >= self.min_wavelength) & (SpectrumWidget.wavelength <= self.max_wavelength)
        filtered_wavelengths = SpectrumWidget.wavelength[mask]
        filtered_data = np.array(self.data)[mask]

        spd_filtered = np.vstack((filtered_wavelengths, filtered_data))
        self.pc.axes.clear()
        plot_spectrum_colors(spd=spd_filtered, axh=self.pc.axes)
        self.pc.draw()
        
class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width= 1, height=1, dpi=95):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
        
