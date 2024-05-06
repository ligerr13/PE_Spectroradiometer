from PyQt6.QtCore import  QSize
from PyQt6.QtWidgets import QTabBar, QPushButton  
from PyQt6.QtGui import QIcon 
import pickle 
from src.workspaceTemplate import WorkspaceDesignWidget


class TabManager:
    def __init__(self, ui_main_window):
        self.tab_widget = ui_main_window.tabWidget
        self.tab_count = 0

    def setup_connections(self, signal_bus):
        signal_bus.closeWorkspace.connect(lambda: self.remove_page(self.get_current_page_index()))
    
    def add_page(self, page_widget, page_name):
        """
        Add a new page to the TabWidget.

        :param page_widget: The QWidget associated with the new page
        :param page_name: The name of the new page
        """
        
        index = self.tab_widget.addTab(page_widget, page_name)
        closeButton = QPushButton()
        closeButton.setIcon(QIcon("../resources/icons/close-2.png"))
        closeButton.setIconSize(QSize(10,10))
        closeButton.clicked.connect(lambda: self.remove_page(index))
        self.tab_widget.tabBar().setTabButton(index, QTabBar.ButtonPosition.RightSide, closeButton)
        self.tab_count += 1

    def remove_page(self, index):
        """
        Remove the page at the specified index.

        :param index: The index of the page to be removed
        """
        self.tab_widget.removeTab(index)
        self.tab_count -= 1

    def get_current_page_index(self):
        """
        Get the index of the current page.

        :return: The index of the current page
        """
        return self.tab_widget.currentIndex()

    def get_current_page_widget(self):
        """
        Get the QWidget associated with the current page.

        :return: The QWidget associated with the current page
        """
        return self.tab_widget.currentWidget()
    
    #NOT POSSIBLE 
    def save_page_to_file(self, wdwObject: WorkspaceDesignWidget, file_name: str): 
        """
        Save the current page's QWidget to a file using pickle.

        :param filename: The name of the file to save to
        """
        with open(file_name + ".pickle", 'wb') as f:
                pickle.dump(wdwObject, f)