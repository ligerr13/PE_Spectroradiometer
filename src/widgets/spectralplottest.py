from PyQt6.QtWidgets import QWidget, QVBoxLayout
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib import cm

plt.style.use('dark_background')

class SpectralPlotWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.spectral_data = None
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.plot_canvas = MplCanvas(self)
        layout.addWidget(self.plot_canvas)

    def set_spectral_data(self, data):
            self.spectral_data = data
            self.plot_data()

    def plot_data(self):
        intensities = [float(value) for value in self.spectral_data.split(",")]
        wavelengths = np.arange(380, 380 + int(len(intensities)), 1)
        


        self.plot_canvas.axes.plot(wavelengths, intensities, color="black")
        colors = cm.nipy_spectral(np.linspace(0, 1 - ((780 - (380+len(intensities))) / 400), len(intensities)))
        for i in range(len(intensities) - 1):
            self.plot_canvas.axes.fill_between(wavelengths[i:i+2], intensities[i:i+2], color=colors[i])

        self.plot_canvas.axes.set_xlabel('Wavelength (nm)')
        self.plot_canvas.axes.set_ylabel('Intensity')
        self.plot_canvas.axes.set_title(f'Spectral Data 380 - {380 + int(len(intensities))}')
        self.plot_canvas.draw()

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)