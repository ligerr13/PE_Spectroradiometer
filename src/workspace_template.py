import os
from PyQt6.QtWidgets import QApplication, QWidget, QTabBar, QSplitter,QVBoxLayout, QLabel,QTableWidgetItem, QTableWidget, QCheckBox, QGridLayout,QHBoxLayout,QDialog, QScrollArea, QSplitterHandle,QGraphicsView, QGraphicsProxyWidget, QGraphicsScene, QMenu, QGraphicsLineItem, QTreeWidgetItem, QPushButton, QSizePolicy, QHeaderView, QStyledItemDelegate, QStyle
from PyQt6.QtGui import QColor, qRgb, QTransform, QCursor, QStandardItem, QIcon, QFont, QFontMetrics, QPaintEvent, QPen, QPainter, QPainterPath
from PyQt6.QtCore import  Qt, QLineF, QEvent, QPoint, QSize, QObject, Qt, pyqtSignal, pyqtSlot
from PyQt6 import QtCore
import json
from pathlib import Path

from src.objects.editSettingsContextMenu import Ui_Form
from src.objects.workspaceDesignFomr import Ui_WorkspaceDesignForm
from src.objects.workspace_data_table import Ui_Form as WDataTableUi_Form
from src.objects.data_table_filter import Ui_Form as WDataTableFilterUi_Form
from src.signals.signals import NodeBoardSignalBus
from src.dialogs.widgetCreatorDialog import WidgetCreatorDialog
from src.widgets.locus_widget import LocusWidget, LocusConfig
from src.widgets.spectrum_widget import SpectrumWidget
from src.widgets.daylight_locus_widget import DaylightLocusConfig, DaylightLocusWidget
from src.signals.signals import WorkspaceSignalBus
from src.dialogs.textToSceneDialog import TextToSceneDialog

from src.globals.utils import add_file_to_tree, convert_numpy, open_dialog, is_valid_measurement_file, get_file_date
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

# class ImportOptionsWidget(QWidget):
#     optionsSelected = pyqtSignal(list)

#     def __init__(self, parent=None):
#         super().__init__(parent)

#         self.checkboxes = []

#         layout = QVBoxLayout(self)

#         scroll_area = QScrollArea(self)
#         scroll_area.setWidgetResizable(True)

#         check_widget = QWidget()
#         self.check_layout = QVBoxLayout()
#         check_widget.setLayout(self.check_layout)

#         scroll_area.setWidget(check_widget)
#         layout.addWidget(scroll_area)

#         apply_btn = QPushButton("Apply")
#         apply_btn.clicked.connect(self.on_apply)

#         layout.addWidget(apply_btn)

#         self.setLayout(layout)

#         checkbox_data_list = [
#             ICheckBoxData(text="Speed Mode", key="Speed mode", imported=False),
#             ICheckBoxData(text="Sync mode", key="Sync mode", imported=False),
#             ICheckBoxData(text="Integration time", key="Integration time", imported=False),
#             ICheckBoxData(text="Internal ND filter", key="Internal ND filter", imported=False),
#             ICheckBoxData(text="Optional close-up lens", key="Optional close-up lens", imported=False),
#             ICheckBoxData(text="Optional external ND filter", key="Optional external ND filter", imported=False),
#             ICheckBoxData(text="Measurement angle", key="Measurement angle", imported=False),
#             ICheckBoxData(text="Calibration channel", key="Calibration channel", imported=False),

#             # Colorimetric
#             ICheckBoxData(text="Le", key="Le", imported=False),
#             ICheckBoxData(text="Lv", key="Lv", imported=False),
#             ICheckBoxData(text="X", key="X", imported=False),
#             ICheckBoxData(text="Y", key="Y", imported=False),
#             ICheckBoxData(text="Z", key="Z", imported=False),
#             ICheckBoxData(text="x", key="x", imported=False),
#             ICheckBoxData(text="y", key="y", imported=False),
#             ICheckBoxData(text="u'", key="u'", imported=False),
#             ICheckBoxData(text="v'", key="v'", imported=False),
#             ICheckBoxData(text="T", key="T", imported=False),
#             ICheckBoxData(text="delta uv", key="delta uv", imported=False),
#             ICheckBoxData(text="lambda d", key="lambda d", imported=False),
#             ICheckBoxData(text="Pe", key="Pe", imported=False),
#             ICheckBoxData(text="X10", key="X10", imported=False),
#             ICheckBoxData(text="Y10", key="Y10", imported=False),
#             ICheckBoxData(text="Z10", key="Z10", imported=False),
#             ICheckBoxData(text="x10", key="x10", imported=False),
#             ICheckBoxData(text="y10", key="y10", imported=False),
#             ICheckBoxData(text="u'10", key="u'10", imported=False),
#             ICheckBoxData(text="v'10", key="v'10", imported=False),
#             ICheckBoxData(text="T10", key="T10", imported=False),
#             ICheckBoxData(text="delta uv10", key="delta uv10", imported=False),
#             ICheckBoxData(text="lambda d10", key="lambda d10", imported=False),
#             ICheckBoxData(text="Pe10", key="Pe10", imported=False),

#             # Spectral groups
#             ICheckBoxData(text="Spectral380To479JsonBuilder", key="Spectral380To479JsonBuilder", imported=False),
#             ICheckBoxData(text="Spectral480To579JsonBuilder", key="Spectral480To579JsonBuilder", imported=False),
#             ICheckBoxData(text="Spectral580To679JsonBuilder", key="Spectral580To679JsonBuilder", imported=False),
#             ICheckBoxData(text="Spectral680To780JsonBuilder", key="Spectral680To780JsonBuilder", imported=False)
#         ]

#         for checkbox_data in checkbox_data_list:
#             checkbox = ICheckBox(checkbox_data)
#             self.add_checkbox(checkbox)

#     def add_checkbox(self, checkbox: ICheckBox):
#         self.checkboxes.append(checkbox)
#         self.check_layout.addWidget(checkbox)

#     def uncheck_option(self, label: str):
#         for checkbox in self.checkboxes:
#             if checkbox.checkbox_data.key == label:
#                 checkbox.setChecked(False)
#                 checkbox.checkbox_data.imported = False

#     def on_apply(self):
#         selected = [
#             checkbox.checkbox_data.key
#             for checkbox in self.checkboxes if checkbox.isChecked()
#         ]
#         self.optionsSelected.emit(selected)
#         self.hide()

class DataTableFilter(QWidget):
    optionsSelected = pyqtSignal(list)
    optionsChanged = pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = WDataTableFilterUi_Form()
        self.ui.setupUi(self)

        self.checkboxes = []
        self.scroll_layout = self.ui.gridLayout_4

        QApplication.instance().installEventFilter(self)
        self.installEventFilter(self)
        self.load_checkboxes()

    def load_checkboxes(self):
        """ICheckBox elemek létrehozása és hozzáadása."""
        
        checkbox_data_list = [
            ICheckBoxData("Speed mode", "Speed Mode"),
            ICheckBoxData("Sync mode", "Sync mode"),
            ICheckBoxData("Integration time", "Integration time"),
            ICheckBoxData("Internal ND filter", "Internal ND filter"),
            ICheckBoxData("Optional close-up lens", "Optional close-up lens"),
            ICheckBoxData("Optional external ND filter", "Optional external ND filter"),
            ICheckBoxData("Measurement angle", "Measurement angle"),
            ICheckBoxData("Calibration channel", "Calibration channel"),

            # Colorimetric
            ICheckBoxData("Le", "Le"),
            ICheckBoxData("Lv", "Lv"),
            ICheckBoxData("X", "X"),
            ICheckBoxData("Y", "Y"),
            ICheckBoxData("Z", "Z"),
            ICheckBoxData("x", "x"),
            ICheckBoxData("y", "y"),
            ICheckBoxData("u'", "u'"),
            ICheckBoxData("v'", "v'"),
            ICheckBoxData("T", "T"),
            ICheckBoxData("delta uv", "delta uv"),
            ICheckBoxData("lambda d", "lambda d"),
            ICheckBoxData("Pe", "Pe"),

            # Spectral
            ICheckBoxData("Spectral380To479JsonBuilder", "Spectral380To479JsonBuilder"),
            ICheckBoxData("Spectral480To579JsonBuilder", "Spectral480To579JsonBuilder"),
            ICheckBoxData("Spectral580To679JsonBuilder", "Spectral580To679JsonBuilder"),
            ICheckBoxData("Spectral680To780JsonBuilder", "Spectral680To780JsonBuilder"),
        ]

        for data in checkbox_data_list:
            cb = ICheckBox(data)
            cb.stateChanged.connect(self.on_checkbox_changed)
            self.checkboxes.append(cb)
            self.scroll_layout.addWidget(cb)

    def on_checkbox_changed(self, state):
        selected = [cb.checkbox_data.key for cb in self.checkboxes if cb.isChecked()]
        self.optionsChanged.emit(selected)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            if self.isVisible():
                if obj is not self:
                    if not self.rect().contains(self.mapFromGlobal(QCursor.pos())):
                        self.hide()
        return super().eventFilter(obj, event)
    
    # def add_apply_button(self):
    #     btn = QPushButton("Apply")
    #     btn.setFixedHeight(35)
    #     btn.setStyleSheet("""
    #         QPushButton {
    #             background-color: rgb(30, 30, 30);
    #             border: 1px solid rgb(60, 60, 60);
    #             border-radius: 5px;
    #             color: white;
    #             font: 700 10pt "Consolas";
    #         }
    #         QPushButton:hover {
    #             background-color: rgb(50, 50, 50);
    #         }
    #     """)
    #     btn.clicked.connect(self.on_apply)
    #     self.scroll_layout.addWidget(btn)

    # def on_apply(self):
    #     selected = [cb.checkbox_data.key for cb in self.checkboxes if cb.isChecked()]
    #     self.optionsSelected.emit(selected)
    #     self.hide()

class WorkspaceDataTable(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = WDataTableUi_Form()
        self.ui.setupUi(self)

        sp = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setSizePolicy(sp)

        self.ui.treeWidget.itemChanged.connect(self.onTreeItemChanged)

        self.filter_widget = DataTableFilter(self)
        self.filter_widget.optionsChanged.connect(self.apply_filter)
        self.filter_widget.hide()

        self.splitter = plitter(Qt.Orientation.Horizontal)
        self.splitter.addWidget(self.ui.widget_2)
        self.splitter.addWidget(self.ui.TableContainer)

        self.ui.horizontalLayout.addWidget(self.splitter)

        self.initMeasurementFiles()

    def apply_filter(self, selected):
        print("Filter applied:", selected)

        WorkspaceSignalBus.instance().update_options.emit(selected)

    def onTreeItemChanged(self, item, column):
        if item.parent() is None:
            return
        
        filename = item.text(0) 
        folder = Path("src/instrument/data")
        file_path = folder / filename

        checked = item.checkState(0) == Qt.CheckState.Checked

        WorkspaceSignalBus.instance().add_file_to_table.emit(file_path, checked)

    def OpenFilterWidget(self):
        target_width = self.ui.widget_2.frameGeometry().width()
        available_height = self.ui.widget_2.frameGeometry().height()

        self.filter_widget.resize(target_width, self.filter_widget.frameGeometry().height())

        if self.filter_widget.sizeHint().height() > available_height:
            self.filter_widget.setParent(self)
            self.filter_widget.setWindowFlags(Qt.WindowType.Widget)
            self.filter_widget.move(0, 0)
        else:
            if self.filter_widget.parent() is not None:
                self.filter_widget.setParent(None)
                self.filter_widget.setWindowFlags(Qt.WindowType.Popup | Qt.WindowType.FramelessWindowHint)

            global_pos = self.ui.widget_2.mapToGlobal(QPoint(0, 0))
            x = global_pos.x()
            y = global_pos.y() + self.ui.widget_2.height()

            self.filter_widget.move(x, y - available_height + 50)

        self.filter_widget.raise_()
        self.filter_widget.show()

    def initMeasurementFiles(self):
        folder = Path("src/instrument/data")
        if not folder.exists():
            return

        for filepath in folder.glob("*.json"):
            try:
                with open(filepath, "r") as f:
                    data = json.load(f)
            except Exception:
                continue

            if not is_valid_measurement_file(data):
                continue

            file_date = get_file_date(filepath)
            add_file_to_tree(self.ui.treeWidget, filepath, file_date)

class TableContainerWidget(QWidget):
    def __init__(self, file_path: Path):
        super().__init__()

        self.imported_files = []
        self.selected_options = []   # csak a FILTER oszlopok!
        
        self.w_data_table = WorkspaceDataTable(self)
        self.table_manager = WorkspaceTable(self.w_data_table.ui.tableWidget)

        # a FILTER-ek változását figyeli
        WorkspaceSignalBus.instance().update_options.connect(self.set_selected_options)
        WorkspaceSignalBus.instance().add_file_to_table.connect(self.onFileToggled)

    def onFileToggled(self, filepath: Path, checked: bool):
        if checked:
            if filepath not in self.imported_files:
                self.imported_files.append(filepath)
        else:
            if filepath in self.imported_files:
                self.imported_files.remove(filepath)

        self.load_data()

    def set_selected_options(self, options: list):
        """
        FILTER CHANGE → update header + reload table
        """
        print("Selected columns:", options)

        # FIX: NINCS több üres oszlop a végén
        self.selected_options = ["", "Measurement"] + options

        table = self.table_manager.table
        table.clear()
        table.setColumnCount(len(self.selected_options))
        table.setHorizontalHeaderLabels(self.selected_options)

        self.load_data()

    def load_data(self):
        self.table_manager.clear_table()

        for fpath in self.imported_files:
            try:
                with open(fpath, "r") as f:
                    data = json.load(f)
                self.insert_data(data, fpath)
            except Exception as e:
                print("Load error:", fpath, e)

    def insert_data(self, data: dict, fpath: Path):
        row_data = [fpath.name]

        # FIX: végre megkapod az utolsó oszlopot is!
        for key in self.selected_options[2:]:
            if "MeasurementJsonBuilder" in data and key in data["MeasurementJsonBuilder"]["Measurement Conditions"]:
                row_data.append(data["MeasurementJsonBuilder"]["Measurement Conditions"][key]["value"])
            elif key in data.get("ColorimetricJsonBuilder", {}).get("Colorimetric Data", {}):
                row_data.append(data["ColorimetricJsonBuilder"]["Colorimetric Data"][key]["value"])
            elif key in data:
                row_data.append(data[key].get("Spectral data", {}).get("value", ""))
            else:
                row_data.append("")

        self.table_manager.add_table_row(row_data)


class WorkspaceTable(QObject):
    def __init__(self, table: QTableWidget, parent=None):
        super().__init__(parent)
        self.table = table

        self.table.setRowCount(0)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["", "Measurement", ""])
        self.table.verticalHeader().hide()
        self.table.setShowGrid(False)

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)

    def clear_table(self):
        self.table.setRowCount(0)

    def add_table_row(self, values: list):
        row = self.table.rowCount()
        self.table.insertRow(row)

        btn = QPushButton("")
        btn.setIcon(QIcon("resources/icons/delete.png"))
        btn.setFixedWidth(40)
        btn.setStyleSheet("background-color: rgb(210,39,48); border: none;")

        self.table.setCellWidget(row, 0, btn)

        bold = QFont()
        bold.setBold(True)

        for col, v in enumerate(values, start=1):
            item = QTableWidgetItem(str(v))
            item.setFont(bold)
            self.table.setItem(row, col, item)

        if row % 2 == 0:
            for col in range(self.table.columnCount()):
                it = self.table.item(row, col)
                if it:
                    it.setBackground(QColor("#191919"))

    def delete_row_of_button(self, btn):
        for row in range(self.table.rowCount()):
            if self.table.cellWidget(row, 0) == btn:
                self.table.removeRow(row)
                break

class plitterHandle(QSplitterHandle):

    handleRelease = pyqtSignal()

    def __init__(self, orientation, parent=None):
        super().__init__(orientation, parent)
        self.is_pressed = False
        self.default_height = 5
        self.pressed_height = 8

        if orientation == Qt.Orientation.Vertical:
            self.setCursor(Qt.CursorShape.SizeVerCursor)
        else:
            self.setCursor(Qt.CursorShape.SizeHorCursor)

    def mousePressEvent(self, event):
        """When handle is pressed, increase its size."""
        
        self.is_pressed == True
        # self.setFixedHeight(self.pressed_height)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        """When the mouse is released, reset the handle size."""
        
        self.is_pressed == True
        # self.setFixedHeight(self.default_height)
        self.handleRelease.emit()
        super().mouseReleaseEvent(event)

class plitter(QSplitter):
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
        """Override createHandle to return an instance of plitterHandle."""
        handle = plitterHandle(self.orientation(), self)
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
        self.splitter = plitter(Qt.Orientation.Vertical)

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