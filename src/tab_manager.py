from PyQt6.QtCore import  QSize, pyqtSignal, QObject, QPoint
from PyQt6.QtWidgets import QTabBar, QPushButton, QMenu
from PyQt6.QtGui import QIcon, QKeySequence
from PyQt6 import QtCore

from src.objects.fileContextMenu import Ui_Form
from src.workspace_landing_page import WorkSpaceLandingPage



class FileContextMenu(QMenu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.file_context_menu = Ui_Form()
        self.file_context_menu.setupUi(self)

        # Submenu for Theme Change


        # Adding actions to submenu
        self.addAction(self.file_context_menu.actionNew_Workspace)
        self.addAction(self.file_context_menu.actionSave)
        self.addAction(self.file_context_menu.actionSave_All)
        self.addAction(self.file_context_menu.actionClose_Workspace)
        self.addAction(self.file_context_menu.actionClose_Window)
        self.file_context_menu.actionClose_Window.setShortcut(QKeySequence("Alt+f4"))

        # Separators
        self.insertSeparator(self.file_context_menu.actionClose_Workspace)
        self.insertSeparator(self.file_context_menu.actionSave)


class TabManager(QObject):
    plusClicked = pyqtSignal()

    def __init__(self, ui_main_window):
        super().__init__()
        self.tabWidget = ui_main_window.tabWidget
        self.tab_count = 0
        self.plusButton = QPushButton()
        self.file_menu_button = QPushButton()
        self.fcu = FileContextMenu()
        
        # Signals
        self.plusButton.clicked.connect(self.plusClicked.emit)
        self.file_menu_button.clicked.connect(self.handle_file_context_menu)
        self.fcu.file_context_menu.actionClose_Workspace.triggered.connect(lambda: self.remove_page(self.get_current_page_index()))
        
        #Calling Methods
        self.setupPlusButton()
        self.setup_file_menu_button()

    def setup_file_menu_button(self):
        """
        Setups the file menu Button.
        """
        self.file_menu_button.setParent(self.tabWidget)
        self.file_menu_button.setFixedSize(40, 40)
        self.file_menu_button.setStyleSheet(""" QPushButton 
            {
                border-radius: 3px;
                padding: 5 5 5 5;
            }""")
        self.file_menu_button.setToolTip("File")
        self.file_menu_button.setIcon(QIcon("../resources/icons/menu.png"))
        self.file_menu_button.move(5, 10)
        self.file_menu_button.setIconSize(QSize(25,25))
        self.file_menu_button.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)


    def setupPlusButton(self):
        """
        Setups the New Worksapce Button.
        """

        self.plusButton.setParent(self.tabWidget)
        self.plusButton.setFixedSize(40, 40)
        self.plusButton.setStyleSheet("""
        QPushButton { 
            background: rgb(25, 25, 25);
            border: 2px solid  rgb(35, 35, 35);
            border-radius: 3px;
            padding: 5 5 5 5;
        }""")
        self.plusButton.setToolTip("New tab")
        self.plusButton.setIcon(QIcon("../resources/icons/plus-symbol-button.png"))
        self.file_menu_button.setIconSize(QSize(25,25))
        self.plusButton.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

        self._move_plus_button()

    def setup_connections(self, signal_bus):
        signal_bus.closeWorkspace.connect(lambda: self.remove_page(self.get_current_page_index()))
    
    def handle_file_context_menu(self):
        sender_button = self.sender()
        global_pos = sender_button.mapToGlobal(sender_button.pos())
        global_pos += QPoint(-5, 32)
        self.fcu.exec(global_pos)
        self.file_menu_button.clearFocus()

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
        closeButton.setIcon(QIcon("../resources/icons/close-2.png"))
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
    
    def __sizeHint(self):
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
        If anything changes make sure the plus button is in the correct location.
        """
        super().tabLayoutChange()

        self._move_plus_button()

    def _move_plus_button(self):
        """
        Move the plus button to the correct location.
        """

        h = self.tabWidget.geometry().top() + 10
        w = self.tabWidget.width()

        if self.__sizeHint().width() >= w:
            self.plusButton.move(self.__sizeHint().width() + 15, h)
        else:
            self.plusButton.move(self.__sizeHint().width(), h)
        