from PyQt6.QtWidgets import QSpacerItem, QWidget, QTabBar, QSplitter,QVBoxLayout, QLabel,QTableWidgetItem, QTableWidget, QCheckBox, QGridLayout,QHBoxLayout,QDialog, QScrollArea, QSplitterHandle,QGraphicsView, QGraphicsProxyWidget, QGraphicsScene, QMenu, QGraphicsLineItem, QTreeWidgetItem, QPushButton, QSizePolicy, QHeaderView, QStyledItemDelegate, QStyle
from PyQt6.QtGui import QColor, qRgb, QTransform, QCursor, QStandardItem, QIcon, QFont, QFontMetrics, QPaintEvent, QPen, QPainter, QPainterPath
from PyQt6.QtCore import  Qt, QLineF, QPointF, QPoint, QSize, QObject, Qt, pyqtSignal, pyqtSlot, QRectF
from PyQt6 import QtCore
import json
from pathlib import Path

from src.objects.editSettingsContextMenu import Ui_Form
from src.objects.workspaceDesignFomr import Ui_WorkspaceDesignForm
from src.signals.signals import NodeBoardSignalBus
from src.dialogs.widgetCreatorDialog import WidgetCreatorDialog
from src.widgets.locus_widget import LocusWidget, LocusConfig
from src.widgets.spectrum_widget import SpectrumWidget
from src.widgets.daylight_locus_widget import DaylightLocusConfig, DaylightLocusWidget
from src.signals.signals import WorkspaceSignalBus
from src.dialogs.textToSceneDialog import TextToSceneDialog

from src.globals.utils import convert_numpy, open_dialog
from src.globals.utils import show_toast, ToastType

class ICheckBoxData(QObject):
    importedChanged = pyqtSignal(bool)
    textChanged = pyqtSignal(str)
    keyChanged = pyqtSignal(str)
    def __init__(self, text: str = "", key: str = "", imported: bool = False):
        super().__init__()
        self.text = text
        self.key = key
        self.imported = imported

        @property
        def text(self):
            return self._text

        @text.setter
        def text(self, value: str):
            if self._text != value:
                self._text = value
                self.textChanged.emit(value)

        @property
        def key(self):
            return self._key

        @key.setter
        def key(self, value: str):
            if self._key != value:
                self._key = value
                self.keyChanged.emit(value)

        @property
        def imported(self):
            return self._imported

        @imported.setter
        def imported(self, value: bool):
            if self._imported != value:
                self._imported = value
                self.importedChanged.emit(value)

    def toggle_imported(self):
        self.imported = not self.imported

class ICheckBox(QCheckBox):
    def __init__(self, checkbox_data: ICheckBoxData):
        super(ICheckBox, self).__init__()
        self.checkbox_data = checkbox_data
        
        self.checkbox_data.importedChanged.connect(self.on_imported_changed)
        self.checkbox_data.textChanged.connect(self.on_text_changed)
        self.checkbox_data.keyChanged.connect(self.on_key_changed)

        self.setText(self.checkbox_data.text)


    def on_imported_changed(self, imported: bool):
        print(f"Imported state changed to: {imported}")

    def on_text_changed(self, text: str):
        print(f"Text changed to: {text}")
        self.setText(text)

    def on_key_changed(self, key: str):
        print(f"Key changed to: {key}")
        
    def on_state_changed(self, state: int):
        print(state)
        if state == Qt.CheckState.Checked:
            self.checkbox_data.imported = True
        else:
            self.checkbox_data.imported = False

class ImportDialog(QDialog):
    optionsSelected = pyqtSignal(list)
    
    def __init__(self):
        super().__init__()
        self.checkboxes = []
        
        self.setWindowTitle("Import Settings")
        self.setFixedSize(300, 300)
        self.setWindowFlags(Qt.WindowType.CustomizeWindowHint)
        layout = QVBoxLayout()

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        check_widget = QWidget()
        self.check_layout = QVBoxLayout()

        check_widget.setLayout(self.check_layout)
        scroll_area.setWidget(check_widget)
        layout.addWidget(scroll_area)

        close_button = QPushButton("Close", self)
        close_button.clicked.connect(self.on_accept)
        
        layout.addWidget(close_button)
        self.setLayout(layout)

        checkbox_data_list = [
            # Conditions
            ICheckBoxData(text="Speed Mode", key="Speed mode", imported=False),
            ICheckBoxData(text="Sync mode", key="Sync mode", imported=False),
            ICheckBoxData(text="Integration time", key="Integration time", imported=False),
            ICheckBoxData(text="Internal ND filter", key="Internal ND filter", imported=False),
            ICheckBoxData(text="Optional close-up lens", key="Optional close-up lens", imported=False),
            ICheckBoxData(text="Optional external ND filter", key="Optional external ND filter", imported=False),
            ICheckBoxData(text="Measurement angle", key="Measurement angle", imported=False),
            ICheckBoxData(text="Calibration channel", key="Calibration channel", imported=False),

            # Colorimetric Data
            ICheckBoxData(text="Le", key="Le", imported=False),
            ICheckBoxData(text="Lv", key="Lv", imported=False),
            ICheckBoxData(text="X", key="X", imported=False),
            ICheckBoxData(text="Y", key="Y", imported=False),
            ICheckBoxData(text="Z", key="Z", imported=False),
            ICheckBoxData(text="x", key="x", imported=False),
            ICheckBoxData(text="y", key="y", imported=False),
            ICheckBoxData(text="u'", key="u'", imported=False),
            ICheckBoxData(text="v'", key="v'", imported=False),
            ICheckBoxData(text="T", key="T", imported=False),
            ICheckBoxData(text="delta uv", key="delta uv", imported=False),
            ICheckBoxData(text="lambda d", key="lambda d", imported=False),
            ICheckBoxData(text="Pe", key="Pe", imported=False),
            ICheckBoxData(text="X10", key="X10", imported=False),
            ICheckBoxData(text="Y10", key="Y10", imported=False),
            ICheckBoxData(text="Z10", key="Z10", imported=False),
            ICheckBoxData(text="x10", key="x10", imported=False),
            ICheckBoxData(text="y10", key="y10", imported=False),
            ICheckBoxData(text="u'10", key="u'10", imported=False),
            ICheckBoxData(text="v'10", key="v'10", imported=False),
            ICheckBoxData(text="T10", key="T10", imported=False),
            ICheckBoxData(text="delta uv10", key="delta uv10", imported=False),
            ICheckBoxData(text="lambda d10", key="lambda d10", imported=False),
            ICheckBoxData(text="Pe10", key="Pe10", imported=False),

            # Spectral Builders
            ICheckBoxData(text="Spectral380To479JsonBuilder", key="Spectral380To479JsonBuilder", imported=False),
            ICheckBoxData(text="Spectral480To579JsonBuilder", key="Spectral480To579JsonBuilder", imported=False),
            ICheckBoxData(text="Spectral580To679JsonBuilder", key="Spectral580To679JsonBuilder", imported=False),
            ICheckBoxData(text="Spectral680To780JsonBuilder", key="Spectral680To780JsonBuilder", imported=False)
        ]


        for checkbox_data in checkbox_data_list:
            checkbox = ICheckBox(checkbox_data)
            self.add_checkbox(checkbox)

    def add_checkbox(self, checkbox: ICheckBox):
        self.checkboxes.append(checkbox)
        self.check_layout.addWidget(checkbox)

    def uncheck_option(self, label: str):
        for checkbox in self.checkboxes:
            if checkbox.checkbox_data.key == label:
                checkbox.setChecked(False)
                checkbox.checkbox_data.imported = False

    def on_accept(self):
        selected_options = [
            checkbox.checkbox_data.key for checkbox in self.checkboxes if checkbox.isChecked()
        ]

        self.optionsSelected.emit(selected_options)
        self.accept()

class TableContainerWidget(QWidget):
    table_count = 0
    load_data_signal = pyqtSignal()

    def __init__(self, file_path: Path):
        super().__init__()

        self.signal_bus  = WorkspaceSignalBus().instance()

        TableContainerWidget.table_count += 1
        self.file_path = file_path
        self.selected_files = []
        self.imported_files = []
        self.selected_options = []
        
        self.import_dialog = ImportDialog()

        self.main_layout = QGridLayout(self)
        self.main_layout.setContentsMargins(1, 1, 1, 1)
        
        self.table = WorkspaceTable()

        self.nav_bar = QWidget()
        self.nav_bar.setFixedWidth(55)
        self.nav_bar.setStyleSheet("""
            background-color: rgb(20, 20, 20); 
            border-right: 1px solid rgba(129, 129, 129, 50);
            border-top: 0;
            border-left:0;
            border-bottom: 0;
            margin: 0 0 0 0;
            padding: 0 0 0 0;
            spacing: 0;
        """)
        self.nav_bar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        
        nav_bar_layout = QGridLayout(self.nav_bar)
        nav_bar_layout.setContentsMargins(1, 1, 1, 1)
        nav_bar_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        nav_bar_layout.setSpacing(3)

        data_selecter_button = QPushButton('', self)
        data_selecter_button.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        data_selecter_button.setIcon(QIcon("resources/icons/plus-symbol-button.png"))
        
        data_selecter_button.setFixedHeight(50)
        data_selecter_button.setFixedWidth(50)

        data_selecter_button.setStyleSheet("""
            border: 0 0 0 0;
            background-color: rgb(25,25,25);
        """)

        import_measurement_data_button = QPushButton('')
        import_measurement_data_button.setIcon(QIcon("resources/icons/import.png"))
        import_measurement_data_button.setFixedHeight(50)
        import_measurement_data_button.setFixedWidth(50)
        import_measurement_data_button.setStyleSheet("""
            border: 0 0 0 0;
            background-color: rgb(25,25,25);
        """)
        
        nav_bar_layout.addWidget(data_selecter_button)
        nav_bar_layout.addWidget(import_measurement_data_button)
        
        self.main_layout.addWidget(self.nav_bar, 0, 0, 2, 1)
        self.main_layout.addWidget(self.table, 0, 1, 1, 2, QtCore.Qt.AlignmentFlag.AlignTop)
        self.setStyleSheet("""
            QWidget {
                background-color: rgb(31,31,31);
                margin: 0 0 0 0;
                padding: 0 0 0 0;
                spacing: 0;
            }
            QLabel {
                padding: 1px;
                font-size: 16px; 
                font-weight: bold;
            }
        """)

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        data_selecter_button.clicked.connect(self.open_import_options)
        import_measurement_data_button.clicked.connect(self.import_measurements_to_workspace_table)
        self.signal_bus.update_options.connect(self.remove_option_from_selected)

    def open_import_options(self):
        if not self.file_path:
            return

        self.import_dialog.optionsSelected.connect(self.set_selected_options)

        if self.import_dialog.exec():
            pass
        
    def import_measurements_to_workspace_table(self):  
        dir = "src/instrument/data"
        opened_files = open_dialog(self, direction=dir)

        if not opened_files:
            return

        for file_path_str in opened_files:
            path_obj = Path(file_path_str)
            if path_obj in self.imported_files:
                print(f"[INFO] File already imported: {path_obj.name}")
                continue

            self.imported_files.append(path_obj)
            print(f"[INFO] Imported: {path_obj.name}")

        self.load_data()

    def remove_imported_file(self, row: int):
        if 0 <= row < len(self.imported_files):
            removed_file = self.imported_files.pop(row)
            print(f"[INFO] Removed from imported_files: {removed_file.name}")
        self.table.removeRow(row)

    def load_data(self):
        self.table.clear_table()

        for file_path in self.imported_files:
            try:
                with open(file_path, 'r') as json_file:
                    data = json.load(json_file)
                    if data:
                        self.insert_data(data, file_path)
            except Exception as e:
                print(f"[ERROR] Could not load {file_path}: {e}")

    def set_selected_options(self, options: list):
        self.selected_options = ['', 'Measurement'] + options + ['']
        self.table.clear_table()
        self.table.setColumnCount(len(self.selected_options))
        self.table.setHorizontalHeaderLabels(self.selected_options)
        self.load_data()


    def remove_option_from_selected(self, label: str, row: int):
        if label in self.selected_options:
            self.selected_options.remove(label)
            self.import_dialog.uncheck_option(label)
            print(f"Option '{label}' removed from selected_options.")
            self.table.delete_row(row)

    def insert_data(self, data: dict, file_path: Path):
        row_data = [file_path.name]
        
        if "MeasurementJsonBuilder" in data and "Measurement Conditions" in data["MeasurementJsonBuilder"]:
            for key in self.selected_options[2:-1]:
                if key in data["MeasurementJsonBuilder"]["Measurement Conditions"]:
                    row_data.append(data["MeasurementJsonBuilder"]["Measurement Conditions"][key]["value"])
                elif key in data:
                    row_data.append(data[key]["Spectral data"]["value"])
                elif key in data.get("ColorimetricJsonBuilder", {}).get("Colorimetric Data", {}):
                    row_data.append(data["ColorimetricJsonBuilder"]["Colorimetric Data"][key]["value"])
                else:
                    row_data.append("")
        
            self.table.add_table_row(row_data)
            self.table.setColumnCount(len(row_data)  + 1)

class WorkspaceTable(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.signal_bus  = WorkspaceSignalBus().instance()

        self.setRowCount(0)
        self.setColumnCount(99)
        self.setHorizontalHeaderLabels(['', 'Measurement', ''])
        self.verticalHeader().hide()
        self.setFixedHeight((self.rowCount()) * 40)

        self.setShowGrid(True)
        self.setGridStyle(QtCore.Qt.PenStyle.NoPen)
        self.setStyleSheet("""
                QTableWidget {
                    background-color: transparent;
                    border: 0 0 0 0;
                    margin: 0 0 0 0;
                    padding: 0 0 0 0;
                    spacing: 0;
                }
            """)
            
        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        self.horizontalHeader().resizeSection(0, 40)

        for i in range(3, self.columnCount()):
            self.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
    
        self.adjust_header_height()

    def adjust_header_height(self):
        header = self.horizontalHeader()
        header.setStyleSheet("""
            QHeaderView::section {
                height: 40px; background-color: rgb(15,15,15);
                border: .5px solid rgb(32,32,32);
                border-top: 0px;
                
            }
        """)
        header.setMinimumHeight(40)
    
    def change_row_background(self, row_number: int, color: QColor):
        for column in range(self.columnCount() + 1):
            item = self.item(row_number, column)
            if item:
                item.setBackground(color)

    def adjust_header_size(self):
        max_label_width = 0
        for row in range(self.rowCount()):
            label_item = self.item(row, 1)
            if label_item:
                bold_font = QFont()
                bold_font.setPointSize(12)
                bold_font.setBold(True)
        
                fm = QFontMetrics(bold_font)
                max_label_width = max(max_label_width, fm.boundingRect(label_item.text()).width())
        return max_label_width


    def delete_row_of_button(self, button: QPushButton):
        for row in range(self.rowCount()):
            if self.cellWidget(row, 0) == button:
                self.parent().remove_imported_file(row)
                break
            
    def delete_row(self, row: int):
        file_item = self.item(row, 1)
        if file_item:
            file_name = file_item.text()
            if hasattr(self.parent(), 'remove_imported_file'):
                self.parent().remove_imported_file(file_name)
        self.removeRow(row)

    def clear_table(self):
        self.setRowCount(0)


    def add_table_row(self, row_data: list):
        row_position = self.rowCount()
        self.insertRow(row_position)

        bold_font = QFont()
        bold_font.setPointSize(12)
        bold_font.setBold(True)

        btn = QPushButton('', self)
        btn.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        btn.setIcon(QIcon("resources/icons/delete.png"))
        btn.setFixedWidth(40)
        btn.setStyleSheet("QPushButton {background-color: rgb(210,39,48);}")
        btn.clicked.connect(lambda _, b=btn: self.delete_row_of_button(b))
        self.setCellWidget(row_position, 0, btn)

        for col, value in enumerate(row_data, start=1):
            item = QTableWidgetItem(str(value))
            item.setFont(bold_font)
            self.setItem(row_position, col, item)

        if row_position % 2 == 0:
            self.change_row_background(row_position, QColor("#191919"))

        self.setFixedHeight((self.rowCount() + 1) * 40)

class WorkspaceTableSplitterHandle(QSplitterHandle):

    handleRelease = pyqtSignal()

    def __init__(self, orientation, parent=None):
        super().__init__(orientation, parent)
        self.is_pressed = False
        self.default_height = 5
        self.pressed_height = 8

        self.setCursor(Qt.CursorShape.SizeVerCursor)

    def mousePressEvent(self, event):
        """When handle is pressed, increase its size."""
        
        self.is_pressed == True
        self.setFixedHeight(self.pressed_height)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        """When the mouse is released, reset the handle size."""
        
        self.is_pressed == True
        self.setFixedHeight(self.default_height)
        self.handleRelease.emit()
        super().mouseReleaseEvent(event)

class WorkspaceTableSplitter(QSplitter):
    toggleButton = pyqtSignal(QWidget, bool)

    def __init__(self, orientation):
        super().__init__(orientation)
        self.splitterMoved.connect(self.onSplitterMoved)
        
        self.rest_anchor = 0
        self.is_hidden = False

        self.setStyle()
        self.setHandleWidth(3)

    def setRestaAnchor(self):
        """Set the rest anchor if the widget is visible."""
        if self.is_hidden == False:
            self.rest_anchor = self.sizes()[0]

    def onSplitterMoved(self, pos: int, index: int):
        """This will check if a widget is hidden and emit a signal."""
        widget = self.widget(index)
        if widget:
            self.is_hidden = widget.visibleRegion().isEmpty()
            self.toggleButton.emit(widget, self.is_hidden)

    def toggleWidget(self, index: int, toggle: bool):
        """Toggles a widget's visibility by resizing the splitter."""
        if toggle:
            self.moveSplitter(self.rest_anchor, index)
        else:
            self.moveSplitter(9999, index)

    def createHandle(self):
        """Override createHandle to return an instance of WorkspaceTableSplitterHandle."""
        handle = WorkspaceTableSplitterHandle(self.orientation(), self)
        handle.handleRelease.connect(self.setRestaAnchor)
        return handle

    def setStyle(self):
        self.setStyleSheet("""
                    QSplitter::handle {
                        background-color: rgb(53, 53, 53);
                    }
                    QSplitter::handle:hover {
                        background-color: rgb(0, 150, 255);
                    }
                """)

class CustomMenu(QMenu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cMenu = Ui_Form()
        self.cMenu.setupUi(self)

        # Submenu for Theme Change
        self.submenu = QMenu("Change Theme")
        self.addMenu(self.submenu)

        # Adding actions to submenu
        self.addAction(self.cMenu.actionShow_Workspace_Grid)
        self.addAction(self.cMenu.actionUndo)
        self.addAction(self.cMenu.actionRedo)
        self.addAction(self.cMenu.actionPaste)
        self.addAction(self.cMenu.actionCopy)
        self.addAction(self.cMenu.actionCut)
        self.addAction(self.cMenu.actionSelect_All)
    

        self.submenu.addAction(self.cMenu.actionDark)
        self.submenu.addAction(self.cMenu.actionLight)

        # Separators
        self.insertSeparator(self.cMenu.actionUndo)
        self.insertSeparator(self.cMenu.actionPaste)
        self.insertSeparator(self.cMenu.actionSelect_All)

class TableTabManager(QObject):
    plusClicked = pyqtSignal()

    def __init__(self, ui_main_window, workspace_name):
        super().__init__()
        self.tabletabwidget = ui_main_window.TabletabWidget
        self.defualt_table_name = workspace_name + "-table"
        self.plusButton = QPushButton("New Table")
        self.tab_count = 0



        self.add_table_page(TableContainerWidget("Table"), f'{self.defualt_table_name}', False)
        self.setupPlusButton()

    def setupPlusButton(self): 
        """
            Setups the New Worksapce Button.
        """

        self.plusButton.setParent(self.tabletabwidget)
        self.plusButton.setFixedSize(3*35, 40)
        self.plusButton.setStyleSheet("""
        QPushButton { 
                background: rgb(25, 25, 25);
                border: 2px solid rgb(35, 35, 35);
                border-radius: 3px;
                padding: 5 5 5 5;
                font: 700 10pt "Consolas";

        }""")
        self.plusButton.setToolTip("New table")
        # self.plusButton.setIcon(QIcon("./resources/icons/plus-symbol-button.png"))
        # self.file_menu_button.setIconSize(QSize(25,25))
        self.plusButton.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

        self._move_plus_button()

        # Signals
        self.plusButton.clicked.connect(self.plusClicked.emit)

    def _move_plus_button(self):
            """
            Move the plus button to the correct location.
            """

            h = self.tabletabwidget.geometry().top() + 5
            w = self.tabletabwidget.width()

            if self._sizeHint().width() >= w:
                self.plusButton.move(self._sizeHint().width() + 20, h)
            else:
                self.plusButton.move(self._sizeHint().width(), h)

    def _sizeHint(self):
        """
        Return the size of the TabBar with increased width for the plus button.
        """
        sizeHint = QTabBar.sizeHint(self.tabletabwidget.tabBar()) 
        width = sizeHint.width()
        height = sizeHint.height()
        return QSize(width + 60, height)
    
    def add_table_page(self, table_widget, page_name, closeable = True):
        """
        Add a new page to the TabWidget.

        :param table_widget: The QWidget associated with the new page
        :param page_name: The name of the new page
        """
       
        max_characters = 30
        character_width = 7
        max_width = max_characters * character_width
        
        display_text = page_name + "  " if len(page_name) <= max_characters else page_name[:max_characters] + '...  '
        text_width = min(len(display_text) * character_width, max_width)
        
        index = self.tabletabwidget.addTab(table_widget, display_text)
        
        self.tabletabwidget.setTabToolTip(index, page_name)
        
        closeButton = QPushButton()
        closeButton.setIcon(QIcon("./resources/icons/close-2.png"))
        closeButton.setIconSize(QSize(10, 10))
        closeButton.clicked.connect(lambda checked, table_widget=table_widget: self.remove_table_page(self.tabletabwidget.indexOf(table_widget)))
        if closeable:
            self.tabletabwidget.tabBar().setTabButton(index, QTabBar.ButtonPosition.RightSide, closeButton)
        self.tabletabwidget.tabBar().setTabData(index, QSize(text_width, 20))
        
        self.tab_count += 1

        self.tabletabwidget.setCurrentWidget(table_widget)

        self._move_plus_button()

    def remove_table_page(self, index):
        """
        Remove the page at the specified index.

        :param index: The index of the page to be removed
        """
        self.tabletabwidget.removeTab(index)
        self.tab_count -= 1
        self._move_plus_button()

class Workspace(QWidget):
    def __init__(self, workspace_name, parent=None):
        super().__init__(parent)
        self.ui = Ui_WorkspaceDesignForm()
        self.ui.setupUi(self)
        self.main = parent
        
        self.workspace_name = workspace_name
        self.explorer = self.ui.treeWidget
        self.grid = self.ui.gridLayout_5
        self.context_menu = CustomMenu(self)
        self.viewScalefactor = 1.15

        self.tabletabmanager = TableTabManager(self.ui, self.workspace_name)
        self.splitter = WorkspaceTableSplitter(Qt.Orientation.Vertical)

        self.splitter.addWidget(self.ui.workspace_container)
        self.splitter.addWidget(self.ui.table_widget_container)

        self.ui.gridLayout_3.addWidget(self.splitter)

        # Views and Scenes
        self.view = self.ui.graphicsView_2
        self.scene = NodeboardGraphicsScene()
        self.button = QPushButton(parent=self.view, text="")

        # Signal Bus
        # self.signal_bus = signal_bus
        self.signal_bus =  WorkspaceSignalBus.instance()

        # Signals
        self.context_menu.cMenu.actionShow_Workspace_Grid.triggered.connect(self.handle_grid_visibility)
        self.signal_bus.update_explorer.connect(self.update_explorer)
        self.splitter.toggleButton.connect(self.toggle_splitter_buttons)
        # self.tabletabmanager.plusClicked.connect(lambda: self.tabletabmanager.add_table_page(TableContainerWidget('asdasd'), f"new-table-{self.tabletabmanager.tab_count + 1}"))
        self.tabletabmanager.plusClicked.connect(lambda: self.tabletabmanager.add_table_page(TableContainerWidget(""), f"new-{self.workspace_name}-{self.tabletabmanager.tab_count + 1}"))
        self.signal_bus.add_widget_to_current_workspace.connect(self.add_widget)


        # QDialogs
        self.widgetCreator = WidgetCreatorDialog()
        self.textCreateToScene = TextToSceneDialog()

        # Calling Methods
        self.group_workspace_group_buttons_to_pages()
        self.view.setScene(self.scene)
        self.generate_grid_tiles_for_scene(self.grid)
        self.context_menu.setMinimumSize(self.context_menu.sizeHint())
        self.handle_menu_widget_visibility(True)
        self.handle_left_menu_tab_visibility(False)
        self.handle_properties_widget_visibility(False)
        self.update_explorer()

    def toggle_splitter_buttons(self, sender: QWidget, is_hidden: bool):
        """Update button state based on splitter movement."""
        if is_hidden:
            self.ui.pushButton_5.setChecked(False)
        else:
            self.ui.pushButton_5.setChecked(True)

    def add_widget(self, scene_widget):
        if scene_widget:
            tab_manager = self.main.get_tab_manager()
            current_workspace = tab_manager.get_current_page_widget()

            if current_workspace == self:
                data = scene_widget.get_widget_data()
                widget_type = scene_widget.__class__.__name__

                match widget_type:
                    case 'SpectrumWidget':
                        clone = SpectrumWidget()
                        clone.configure(data.get('data'), data.get('range')['min'], data.get('range')['max'])
                        clone.setGeometry(
                            data.get('geometry')['x'], 
                            data.get('geometry')['y'], 
                            data.get('geometry')['width'], 
                            data.get('geometry')['height']
                        )
                        self.scene.addWidget(clone)

                    case 'LocusWidget':
                        clone = LocusWidget()
                        clone.configure(
                            data.get('data'), 
                            data.get('config')['cctext'], 
                            data.get('config')['eew'],
                            data.get('config')['dl'], 
                            data.get('config')['bbl'],
                            data.get('config')['d65'])
                        
                        clone.setGeometry(
                            data.get('geometry')['x'], 
                            data.get('geometry')['y'], 
                            data.get('geometry')['width'], 
                            data.get('geometry')['height'])
                        
                        self.scene.addWidget(clone)

                    case 'DaylightLocusWidget':
                        clone = DaylightLocusWidget()
                        clone.configure(
                            data.get('data'), 
                            data.get('config')['ccts'], 
                            data.get('config')['force_daylight_below4000K'],
                        )                        
                        clone.setGeometry(
                            data.get('geometry')['x'], 
                            data.get('geometry')['y'], 
                            data.get('geometry')['width'], 
                            data.get('geometry')['height'])
                        
                        self.scene.addWidget(clone)
                    case _:
                        print(f"Unsupported widget type: {widget_type}")


    @pyqtSlot(bool)
    def toggle_bottom_panel(self, value: bool):
        """Toggle the bottom panel based on button press."""
        index = 1
        self.splitter.toggleWidget(index, value)

    def set_workspace_name(self, workspace_name: str):
        self.workspace_name = workspace_name

    def get_workspace_name(self) -> str:
        return self.workspace_name

    def resizeEvent(self, event):
        self.update_test_button_on_view()
        super().resizeEvent(event)

    def update_test_button_on_view(self, offset = None):
        self.button.setGeometry(QtCore.QRect(self.view.viewport().width() - 80, 5, 75, 35))
        self.button.setStyleSheet("""background: rgb(31,31,31);
                                  border-radius: 3px;
                                  border: 1px solid rgb(41,41,41);
                                  color: rgb(170,170,170);
                                  font: 570 10pt "Consolas";
        """)
        self.button.setText(f"{self.view.viewport().width()}x{self.view.viewport().height()}") 
    
    def update_explorer(self):
        widget_items = self.explorer.findItems("Widget", Qt.MatchFlag.MatchExactly | Qt.MatchFlag.MatchRecursive)
        
        if widget_items:
            for item in widget_items:
                WIDGET_DATA = self.scene.extract_widget_data()

                current_items = {item.child(i).text(0) for i in range(item.childCount())}
                
                new_items = {widget.objectName for widget in WIDGET_DATA}

                for i in reversed(range(item.childCount())):
                    child = item.child(i)
                    if child.text(0) not in new_items:
                        item.removeChild(child)
                
                for objName in new_items:
                    if objName not in current_items:
                        item.addChild(QTreeWidgetItem([objName]))

    def handle_grid_visibility(self, state):
            for gridLines in self.scene.items():
                if isinstance(gridLines, QGraphicsLineItem):
                    gridLines.setVisible(state)
        
    def handle_edit_settings_context_menu(self):
        sender_button = self.sender()
        global_pos = sender_button.mapToGlobal(sender_button.pos())
        global_pos += QPoint(-230, 35)
        self.context_menu.exec(global_pos)
        self.ui.workspaceEditSettingsButton.clearFocus()
        
    def group_workspace_group_buttons_to_pages(self):
         for i, button in enumerate(self.ui.WorkspaceMenuButtonGroup.buttons()):
              self.ui.WorkspaceMenuButtonGroup.setId(button, i)

    def handle_properties_widget_visibility(self, state):
        self.ui.properties_right_panel.setVisible(state)
    #Not the most elegant way to solve this.. has to be a better way to change the style.
    def handle_left_menu_tab_visibility(self, state):
        self.ui.WorkspaceMenuWidget.setVisible(state)
        self.ui.widget_17.setStyleSheet("""
            QWidget {border: 0;}
            QPushButton {
            font: 570 10pt "Consolas";
            color: 	rgb(190, 190, 190);
            padding: 5 5 5 5;
            margin: 0 0 -1 0;
            }
            QPushButton:hover {
                        color: white;
                        background: rgb(40, 40, 40);
                    }
            QPushButton:checked  {
                    border: 0px;
                    border-radius: 0px;
            }
            QPushButton:unchecked  {
                    border: 0px;
                    background-color: transparent;
                    color: 	rgb(171, 171, 171);
            }
            QToolTip{ 
                    font: 12pt;
                    color: rgb(100, 100, 100);
            }""")

    def handle_menu_widget_visibility(self, state):
        if not self.ui.WorkspaceMenuWidget.isVisible():
            self.ui.WorkspaceMenuWidget.setVisible(state)
            self.ui.widget_17.setStyleSheet("""QWidget {border: 0;}
                QPushButton {
                font: 570 10pt "Consolas";
                color: 	rgb(190, 190, 190);
                padding: 5 5 5 5;
                margin: 0 0 -1 0;
                }
                QPushButton:hover {
                            color: white;
                            background:  rgb(40, 40, 40);
                        }
                QPushButton:checked  {
                        border-left: 3px solid rgb(0, 150, 255);
                        border-radius: 0px;
                        background: rgb(40, 40, 40);
                        color:white;
                }
                QPushButton:unchecked  {
                    border: 0px;
                    background-color: transparent;
                    color: 	rgb(171, 171, 171);
                }
                QToolTip{ 
                        font: 12pt;
                        color: rgb(100, 100, 100);
                }""")
            self.update_test_button_on_view()
                
    def handle_create_widget_on_scene(self, selected: bool):
        if selected is not None:
            if  selected == False:
                self.widgetCreator.closePopUp()
            else:
                self.widgetCreator.popUp()
                self.ui.CreateWidgetButton.setChecked(True)

    def handle_scene_drag_mode(self, selected: bool):
        if selected:
            self.view.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
            WIDGET_DATA = self.scene.extract_widget_data()
            for widget in WIDGET_DATA:
                widget.enableMovementSignal.emit(True)
        else:
            self.view.setDragMode(QGraphicsView.DragMode.NoDrag)
            WIDGET_DATA = self.scene.extract_widget_data()
            for widget in WIDGET_DATA:
                widget.enableMovementSignal.emit(False) 

    def handle_scene_select_mode(self, selected: bool):
            try:
                if selected is not None:
                    if selected == False:
                        self.scene.setSelecteButton(None)
                    else:
                        self.scene.setSelecteButton(self.sender())
            except AttributeError as e:
                print("An AttributeError occurred:", e)

    def handle_scene_delete_mode(self, selected: bool):
        if selected is not None:
            if  selected == False:
                self.scene.setDeleteButton(None)
            else:
                self.scene.setDeleteButton(self.sender())

    def handle_scene_zoom_in(self):
        scale_tr = QTransform()
        scale_tr.scale(self.viewScalefactor, self.viewScalefactor)

        tr = self.view.transform() * scale_tr
        if tr.m11() <= 2.0 and tr.m22() <= 2.0:
            self.view.setTransform(tr)

    def handle_scene_zoom_out(self):
        scale_tr = QTransform()
        scale_tr.scale(1 / self.viewScalefactor, 1 / self.viewScalefactor)

        tr = self.view.transform() * scale_tr
        if tr.m11() >= 0.4 and tr.m22() >= 0.4:
            self.view.setTransform(tr)

    def generate_grid_tiles_for_scene(self, grid):
        colorH = QColor(qRgb(31, 31, 31))
        colorV = QColor(qRgb(51, 51, 51))
        vLines = 100
        hLines = 100
        side = 25
        hor = 0
        ver = 0
        subdiv = 100
        leftX, leftY = 0, 0
        rightX, rightY = subdiv * side, 0
        bottomX, bottomY = 0, 0
        topX, topY = 0, subdiv * side

        while ver < vLines:
            ver += 1
            vLine = QLineF(bottomX, bottomY, topX, topY)
            bottomX += side
            topX += side
            self.scene.addLine(vLine, colorH).setZValue(-1)

        while hor < hLines:
            hor += 1
            if hor == 1:
                leftY += side
                rightY += side
                continue
            hLine = QLineF(leftX, leftY, rightX, rightY)
            leftY += side
            rightY += side
            self.scene.addLine(hLine, colorV).setZValue(-1)

        grid.addWidget(self.view, 0, 1, 1, 1)

    def handle_add_text_to_scene(self):
        print("Opening text dialog or widget...")
        self.textCreateToScene.popUp()
    
    def handle_add_image_to_scene(self):
        print("Opening image dialog or widget...")

    def save_workspace(self, file_name: str):
        WIDGET_DATA = self.scene.extract_widget_data()
        
        DATA = [widget.get_widget_data() for widget in WIDGET_DATA]
        
        WORKSPACE_DATA = {
        "workspace": self.workspace_name,
        "widgets": DATA }

        with open(file_name, 'w') as file:
            json.dump(WORKSPACE_DATA, file, indent=4, default=convert_numpy)
        
        # show_toast("Workscape Saved!", 3000, ToastType.SUCCESS)
    
    def load_workspace(self, file_name: str):
        try:
            with open(file_name, 'r') as file:
                LOADED = json.load(file)

            if not isinstance(LOADED, dict):
                raise ValueError("Loaded data is not a valid dictionary.")

            workspace_name = LOADED.get('workspace')
            if not workspace_name:
                raise ValueError("Workspace name is missing or invalid.")

            WIDGETS_DATA = LOADED.get('widgets', [])
            if not isinstance(WIDGETS_DATA, list):
                raise ValueError("Widgets data is not a valid list.")

            for WIDGET in WIDGETS_DATA:
                if not isinstance(WIDGET, dict):
                    continue

                widget_type = WIDGET.get('type')
                sub_type = WIDGET.get('sub-type')

                if widget_type == 'SceneWidget':
                    if sub_type == 'Spectrum-Color':
                        try: 
                            widget = SpectrumWidget()
                            widget.setObjectName(WIDGET.get('unique_name', 'DefaultID'))
                            raw_spectral_data = WIDGET.get('data', [])
                            min_wl = WIDGET.get('range')['min']
                            max_wl = WIDGET.get('range')['max']

                            if isinstance(raw_spectral_data, list):
                                widget.configure(raw_spectral_data, min_wl, max_wl)

                        except Exception as widget_error:
                            print(f"An Error has happend while creating spectrum widgets: {widget_error}")


                    elif sub_type == 'Locus':
                        try:
                            widget = LocusWidget()
                            widget.setObjectName(WIDGET.get('unique_name', 'DefaultID'))
                            raw_colorimetric_data = WIDGET.get('data', [])
                            colorimetric_config =   WIDGET.get('config', {})
                            config = LocusConfig(
                                cctext=colorimetric_config.get('cctext', False),
                                eew=colorimetric_config.get('eew', False),
                                bbl=colorimetric_config.get('bbl', True),
                                dl=colorimetric_config.get('dl', False),
                                d65=colorimetric_config.get('d65', False)
                            )

                           
                            widget.configure(
                                data=raw_colorimetric_data,
                                cctext=config.cctext,
                                eew=config.eew,
                                dl=config.dl,
                                bbl=config.bbl,
                                d65=config.d65
                            )
                        except Exception as widget_error:
                            print(f"An Error has happend while creating locus widgets: {widget_error}")

                    elif sub_type == 'DaylightLocus':
                        try:
                            widget = DaylightLocusWidget()
                            widget.setObjectName(WIDGET.get('unique_name', 'DefaultID'))
                            raw_ccts_data = WIDGET.get('data', [])
                            daylight_config =   WIDGET.get('config', {})
                            config = DaylightLocusConfig(
                                ccts=daylight_config.get('ccts', []),
                                force_daylight_below4000K=daylight_config.get('force_daylight_below4000K', False)
                            )

                            widget.configure(
                                data=raw_ccts_data,
                                ccts=config.ccts,
                                force_daylight_below4000K=config.force_daylight_below4000K
                            )
                        except Exception as widget_error:
                            print(f"An Error has happend while creating locus widgets: {widget_error}")

                    else:
                        continue

                    try:
                        geometry = WIDGET.get('geometry', {})
                        x, y, width, height = (
                            geometry.get('x'),
                            geometry.get('y'),
                            geometry.get('width'),
                            geometry.get('height')
                        )

                        if all(isinstance(val, (int, float)) for val in [x, y, width, height]):
                            widget.setGeometryProperties(x, y, width, height)
                        else:
                            raise ValueError("Invalid geometry values.")

                        self.scene.addWidget(widget)

                    except Exception as widget_error:
                        print(f"An Error has happend while loading widgets: {widget_error}")

            self.update_explorer()
        except FileNotFoundError:
            print("The file not found!")
        except json.JSONDecodeError:
            print("Invalid JSON file!")
        except ValueError as ve:
            print(f"Invalid data: {ve}")
        except Exception as e:
            print(f"Unknown error: {e}")

class NodeboardGraphicsScene(QGraphicsScene):

    def __init__(self, parent=None):
        QGraphicsScene.__init__(self, parent)
        # Signalbus
        self.nodeboard_signal_bus = NodeBoardSignalBus()
        self.signal_bus =  WorkspaceSignalBus.instance()

        # Buttons
        self.SelectButton = None
        self.DeleteButton = None
        self.CreateWidgetButon = None

        # Widgets
        self.selectedWidget = None

        # Signals
        self.nodeboard_signal_bus.widgetSelectedSignal.connect(self.onSelectWidget)
        self.nodeboard_signal_bus.widgetDeselectedSignal.connect(self.onDeselectWidget)
        self.nodeboard_signal_bus.widgetDeletedSignal.connect(self.onWidgetDelete)
        #Calling methods

    # Setters
    def setSelecteButton(self, button):
        self.SelectButton = button

    def setDeleteButton(self, button):
        self.DeleteButton = button
        if button and button.isChecked() and self.selectedWidget:
            self.nodeboard_signal_bus.onWidgetDeletedSignalEmit(self.selectedWidget)
    
    def mousePressEvent(self, event):
        if self.SelectButton and self.SelectButton.isChecked():
            item = self.itemAt(event.scenePos(), QTransform())
            if isinstance(item, QGraphicsProxyWidget):
                if item != self.selectedWidget:
                    self.nodeboard_signal_bus.onWidgetDeselectedSignalEmit(self.selectedWidget)
                    self.selectedWidget = item
                    self.nodeboard_signal_bus.onWidgetSelectedSignalEmit(self.selectedWidget)
            else:
                self.nodeboard_signal_bus.onWidgetDeselectedSignalEmit(self.selectedWidget)
        else:
            self.nodeboard_signal_bus.onWidgetDeselectedSignalEmit(self.selectedWidget)
        super().mousePressEvent(event)

    def onWidgetDelete(self, deleted: QGraphicsProxyWidget):
        if isinstance(deleted, QGraphicsProxyWidget):
            self.nodeboard_signal_bus.onWidgetDeselectedSignalEmit(deleted)
            self.removeItem(deleted)
            self.signal_bus.emitUpdateExplorer()
                
    def onSelectWidget(self, selected: QGraphicsProxyWidget):
        if isinstance(selected, QGraphicsProxyWidget):
            selected.widget().setStyleSheet("QWidget {\nbackground-color: rgb(75, 75, 75);\nborder-radius: 5px; }")
            self.signal_bus.emitWidgetDataToPorpertyEditor(property_holder=selected.widget())

    def onDeselectWidget(self, deselected: QGraphicsProxyWidget):
        if isinstance(deselected, QGraphicsProxyWidget):
            deselected.widget().setStyleSheet("QWidget {\nbackground-color: rgb(45, 45, 45);\nborder-radius: 5px; }")
            self.selectedWidget = None
            pass

    def extract_widget_data(self):
        widget_data = []

        for item in self.items():
            if isinstance(item, QGraphicsProxyWidget):
                widget_item = item
                widget = widget_item.widget()

                if widget:
                    widget_data.append(widget)

        return widget_data