from PyQt6.QtCore import QObject, QLineF, QPointF, pyqtSignal
from PyQt6.QtWidgets import QGraphicsScene, QWidget, QGraphicsProxyWidget, QWidget
from PyQt6.QtGui import QColor, qRgb, QTransform

class TabManager:
    def __init__(self, ui_main_window):
        self.tab_widget = ui_main_window.tabWidget
        self.tab_count = 0
    
    def setup_connections(self, signal_bus):
        signal_bus.closeWorkspace.connect(lambda: self.remove_page(self.get_current_page_index()))
    
    def add_page(self, page_widget, page_name):
        """
        Új lap hozzáadása a TabWidget-hez.

        :param page_widget: Az új oldalhoz tartozó QWidget
        :param page_name: Az új oldal neve
        """
        self.tab_widget.addTab(page_widget, page_name)
        self.tab_count += 1

    def remove_page(self, index):
        """
        Lap eltávolítása a megadott indexű helyről.

        :param index: Az eltávolítandó lap indexe
        """
        self.tab_widget.removeTab(index)
        self.tab_count -= 1

    def get_current_page_index(self):
        """
        Az aktuális oldal indexének lekérdezése.

        :return: Az aktuális oldal indexe
        """
        return self.tab_widget.currentIndex()

    def get_current_page_widget(self):
        """
        Az aktuális oldalhoz tartozó QWidget lekérdezése.

        :return: Az aktuális oldalhoz tartozó QWidget
        """
        return self.tab_widget.currentWidget()
