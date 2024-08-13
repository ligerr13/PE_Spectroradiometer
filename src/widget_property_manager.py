from PyQt6.QtCore import  QSize, pyqtSignal, QObject, QPoint, Qt
from PyQt6.QtWidgets import QTabBar, QPushButton, QMenu, QMenuBar
from PyQt6.QtGui import QIcon, QKeySequence
from PyQt6 import QtCore



class WidgetPropertyManager(QObject):
    selected = pyqtSignal()

    def __init__(self, ui_main_window):
        super().__init__()
        # self.tabWidget = ui_main_window.tabWidget

        # Signals
        
        #Calling Methods
        
    def change_page(self):
        """
        Changes the page when the first selection occurs or no widgets on the board.
        """
        pass