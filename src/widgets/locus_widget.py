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
from luxpy import plotSL, plot_color_data
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from dataclasses import dataclass

@dataclass
class LocusConfig:
    cctext: bool = False
    eew: bool = False
    bbl: bool = True
    dl: bool = False
    d65: bool = False

class LocusWidget(SceneWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.data = None
        self.config = LocusConfig()

        self.plt = plt
        self.sub_type = 'Locus'
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
                'cctext': self.config.cctext,
                'eew':  self.config.eew,
                'dl':   self.config.dl,
                'bbl':  self.config.bbl,
                'd65':  self.config.d65
            }
        }
    
    def configure(self, data, cctext, eew, dl, bbl, d65):
        self.data = data
        self.config.cctext = cctext
        self.config.eew = eew
        self.config.dl = dl 
        self.config.bbl = bbl 
        self.config.d65 = d65 

        axh = plotSL(cspace = 'Yuv', cieobs = self.cieobs, show = False,\
                 BBL = bbl, EEW = eew, D65 = d65, DL = dl, diagram_colors = True, axh = self.pc.axes, cctlabels=cctext)
        
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