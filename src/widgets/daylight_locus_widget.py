from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import QPoint, Qt
from PyQt6.QtGui import QMouseEvent
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib import cm
from .scene_widget import SceneWidget
from luxpy import plotDL, plot_color_data
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from dataclasses import dataclass
import numpy as np

@dataclass
class DaylightLocusConfig:
    ccts: list[float] = None
    force_daylight_below4000K: bool = False

class DaylightLocusWidget(SceneWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.data = None
        self.config = DaylightLocusConfig()

        self.plt = plt
        self.sub_type = 'DaylightLocus'
        self.cieobs = '1931_2'

        self.plt.style.use('seaborn-v0_8')

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
            'data': self.data,
            'config': {
                'ccts': self.config.ccts,
                'force_daylight_below4000K':  self.config.force_daylight_below4000K,
            }
        }
    
    def configure(self, data, ccts, force_daylight_below4000K):
        self.data = data
        self.config.force_daylight_below4000K = force_daylight_below4000K

        if not ccts:
            self.config.ccts = []

        self.config.ccts = ccts

        axh = plotDL(cspace = 'Yuv', cieobs = self.cieobs, show = False,\
                force_daylight_below4000K = False, axh = self.pc.axes, ccts=self.config.ccts)
        
        Y = data["Y"]
        u = data["u'"]
        v = data["v'"]
        
        plot_color_data(u, v, formatstr = 'go', axh = axh, label = 'Yuv')

        self.pc.draw()
        
class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width= 1, height=1, dpi=95):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)