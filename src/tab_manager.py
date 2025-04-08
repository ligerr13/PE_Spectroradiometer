from PyQt6.QtCore import  QSize, pyqtSignal, QObject, QPoint, Qt
from PyQt6.QtWidgets import QTabBar, QPushButton, QMenu, QMenuBar, QWidget
from PyQt6.QtGui import QIcon, QKeySequence
from PyQt6 import QtCore
from src.globals.utils import show_toast, ToastType

class TabManager(QObject):
    plusClicked = pyqtSignal()

    def __init__(self, ui_main_window):
        super().__init__()
        self.tabWidget = ui_main_window.tabWidget
        self.tab_count = 0
        self.plusButton = QPushButton()
        self.file_menu_button = QPushButton()
        
        # Signals
        self.plusButton.clicked.connect(self.plusClicked.emit)
        
        #Calling Methods
        self.setupPlusButton()
        self.setup_file_menu_button()

    def setup_file_menu_button(self):
        """
        Setups the file menu Button.
        """
        self.file_menu_button.setParent(self.tabWidget)
        self.file_menu_button.setFixedSize(43, 43)
        self.file_menu_button.setStyleSheet(""" QPushButton 
            {
                border-radius: 2px;
            }
            QPushButton:hover {
                background-color: rgb(31,31,31);
            }""")
        self.file_menu_button.setToolTip("File")
        self.file_menu_button.setIcon(QIcon("./resources/icons/menu.png"))
        self.file_menu_button.move(5, 5)
        self.file_menu_button.setIconSize(QSize(25,25))
        self.file_menu_button.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

    def setupPlusButton(self):
        """
        Setups the New Worksapce Button.
        """

        self.plusButton.setParent(self.tabWidget)
        self.plusButton.setFixedSize(35, 35)
        self.plusButton.setStyleSheet("""
        QPushButton { 
            background: rgb(25, 25, 25);
            border: 2px solid  rgb(35, 35, 35);
            border-radius: 3px;
            padding: 5 5 5 5;
        }""")
        self.plusButton.setToolTip("New tab")
        self.plusButton.setIcon(QIcon("./resources/icons/plus-symbol-button.png"))
        self.file_menu_button.setIconSize(QSize(25,25))
        self.plusButton.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

        self._move_plus_button()

    def setup_connections(self, signal_bus):
        signal_bus.closeWorkspace.connect(lambda: self.remove_page(self.get_current_page_index()))

    def add_page(self, workspace, page_name):
        """
        Add a new page to the TabWidget.

        :param workspace: The QWidget associated with the new page
        :param page_name: The name of the new page
        """
       
        max_characters = 30
        character_width = 7
        max_width = max_characters * character_width
        
        display_text = page_name + "  " if len(page_name) <= max_characters else page_name[:max_characters] + '...  '
        text_width = min(len(display_text) * character_width, max_width)
        
        index = self.tabWidget.addTab(workspace, display_text)
        
        self.tabWidget.setTabToolTip(index, page_name)
        
        closeButton = QPushButton()
        closeButton.setIcon(QIcon("./resources/icons/close-2.png"))
        closeButton.setIconSize(QSize(10, 10))
        closeButton.clicked.connect(lambda checked, workspace=workspace: self.remove_page(self.tabWidget.indexOf(workspace)))
        
        self.tabWidget.tabBar().setTabButton(index, QTabBar.ButtonPosition.RightSide, closeButton)
        self.tabWidget.tabBar().setTabData(index, QSize(text_width, 20))
        
        self.tab_count += 1

        self.tabWidget.setCurrentWidget(workspace)

        self._move_plus_button()
        
    def remove_page(self, index):
        """
        Remove the page at the specified index.

        :param index: The index of the page to be removed
        """
        self.tabWidget.removeTab(index)
        self.tab_count -= 1
        self._move_plus_button()

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
    
    def _sizeHint(self):
        """
        Return the size of the TabBar with increased width for the plus button.
        """
        sizeHint = QTabBar.sizeHint(self.tabWidget.tabBar()) 
        width = sizeHint.width()
        height = sizeHint.height()
        return QSize(width + 60, height)

    def resizeEvent(self, event):
        """
        Resize the widget and make sure the plus button is in the correct location.
        """
        super().resizeEvent(event)

    def tabLayoutChange(self):
        """
        This virtual handler is called whenever the tab layout changes.
        """
        super().tabLayoutChange()

        self._move_plus_button()

    def _move_plus_button(self):
        """
        Move the plus button to the correct location.
        """

        h = self.tabWidget.geometry().top() + 10
        w = self.tabWidget.width()

        if self._sizeHint().width() >= w:
            self.plusButton.move(self._sizeHint().width() + 20, h)
        else:
            self.plusButton.move(self._sizeHint().width(), h)
        
    def get_page_by_tabname(self, tab_name: str) -> int:
        try:
            index = self.tabWidget.indexOf(self.tabWidget.findChild(QWidget, tab_name))
            return index
        except Exception as e:
            message = f"Error finding page: \n{e}"
            show_toast(message, 7000, ToastType.ERROR)
            return -1