from PyQt6.QtCore import  QSize, pyqtSignal, QObject
from PyQt6.QtWidgets import QTabBar, QPushButton  , QWidget
from PyQt6.QtGui import QIcon
import pickle 
from src.workspace_template import Workspace


class TabManager(QObject):
    plusClicked = pyqtSignal()

    def __init__(self, ui_main_window):
        super().__init__()
        self.tabWidget = ui_main_window.tabWidget
        self.tab_count = 0
        self.plusButton = QPushButton()
        self.plusButton.clicked.connect(self.plusClicked.emit)
        self.setupPlusButton()

    def setupPlusButton(self):
        """
        Setups the New Widget Button.
        """

        self.plusButton.setParent(self.tabWidget)
        self.plusButton.setFixedSize(40, 40)
        self.plusButton.setStyleSheet("""
        QPushButton { 
            background: rgb(25, 25, 25);
            border: 1px solid  rgb(35, 35, 35);
            border-radius: 2px;
            padding: 5 5 5 5;
        }""")
        self.plusButton.setToolTip("New tab")
        self.plusButton.setIcon(QIcon("../resources/icons/plus-symbol-button.png"))

        self.__movePlusButton()
        


    def setup_connections(self, signal_bus):
        signal_bus.closeWorkspace.connect(lambda: self.remove_page(self.get_current_page_index()))
    
    def add_page(self, page_widget, page_name):
        """
        Add a new page to the TabWidget.

        :param page_widget: The QWidget associated with the new page
        :param page_name: The name of the new page
        """
       
        max_characters = 30
        character_width = 7
        max_width = max_characters * character_width
        
        display_text = page_name + "  " if len(page_name) <= max_characters else page_name[:max_characters] + '...  '
        text_width = min(len(display_text) * character_width, max_width)
        
        index = self.tabWidget.addTab(page_widget, display_text)
        
        self.tabWidget.setTabToolTip(index, page_name)
        
        closeButton = QPushButton()
        closeButton.setIcon(QIcon("../resources/icons/close-2.png"))
        closeButton.setIconSize(QSize(10, 10))
        closeButton.clicked.connect(lambda checked, page_widget=page_widget: self.remove_page(self.tabWidget.indexOf(page_widget)))
        
        self.tabWidget.tabBar().setTabButton(index, QTabBar.ButtonPosition.RightSide, closeButton)
        self.tabWidget.tabBar().setTabData(index, QSize(text_width, 20))
        
        self.tab_count += 1

        self.tabWidget.setCurrentWidget(page_widget)

        self.__movePlusButton()


    def remove_page(self, index):
        """
        Remove the page at the specified index.

        :param index: The index of the page to be removed
        """
        self.tabWidget.removeTab(index)
        self.tab_count -= 1
        self.__movePlusButton()


    def get_current_page_index(self):
        """
        Get the index of the current page.

        :return: The index of the current page
        """
        return self.tabWidget.currentIndex()

    def get_current_page_widget(self):
        """
        Get the QWidget associated with the current page.

        :return: The QWidget associated with the current page
        """
        return self.tabWidget.currentWidget()
    
    #NOT POSSIBLE 
    def save_page_to_file(self, wdwObject: Workspace, file_name: str): 
        """
        Save the current page's QWidget to a file using pickle.

        :param filename: The name of the file to save to
        """
        with open(file_name + ".pickle", 'wb') as f:
                pickle.dump(wdwObject, f)


    def __sizeHint(self):
        """
        Return the size of the TabBar with increased width for the plus button.
        """
        sizeHint = QTabBar.sizeHint(self.tabWidget.tabBar()) 
        width = sizeHint.width()
        height = sizeHint.height()
        return QSize(width + 10, height)

    def resizeEvent(self, event):
        """
        Resize the widget and make sure the plus button is in the correct location.
        """
        super().resizeEvent(event)

    def tabLayoutChange(self):
        """
        This virtual handler is called whenever the tab layout changes.
        If anything changes make sure the plus button is in the correct location.
        """
        super().tabLayoutChange()

        self.__movePlusButton()

    def __movePlusButton(self):
        """
        Move the plus button to the correct location.
        """

        h = self.tabWidget.geometry().top() + 5
        w = self.tabWidget.width()

        if self.__sizeHint().width() >= w:
            self.plusButton.move(w - 100, h)
        else:
            self.plusButton.move(self.__sizeHint().width(), h)
        