from PyQt6.QtWidgets import QWidget, QSplitter,QVBoxLayout, QLabel,QTableWidgetItem, QTableWidget, QCheckBox, QGridLayout,QHBoxLayout,QDialog, QScrollArea, QSplitterHandle,QGraphicsView, QGraphicsProxyWidget, QGraphicsScene, QMenu, QGraphicsLineItem, QTreeWidgetItem, QPushButton, QSizePolicy, QHeaderView, QStyledItemDelegate, QStyle
from PyQt6.QtGui import QColor, qRgb, QTransform, QCursor, QStandardItem, QIcon, QFont, QFontMetrics, QPaintEvent, QPen, QPainter, QPainterPath
from PyQt6.QtCore import  Qt, QLineF, QPointF, QPoint, QSize, QObject, Qt, pyqtSignal, pyqtSlot, QRectF
from PyQt6 import QtCore
import json
from pathlib import Path

from src.objects.editSettingsContextMenu import Ui_Form
from src.objects.workspaceDesignFomr import Ui_WorkspaceDesignForm
from src.signals.signals import NodeBoardSignalBus
from src.dialogs.widgetCreatorDialog import WidgetCreatorDialog
from src.widgets.spectralplottest import SpectralPlotWidget
from src.signals.signals import WorkspaceSignalBus
from src.dialogs.textToSceneDialog import TextToSceneDialog

from src.globals.utils import open_dialog
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
        self.selected_options = []
        
        self.import_dialog = ImportDialog()

        main_layout = QGridLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 15)
        
        title_layout = QHBoxLayout()
        
        btn = QPushButton('', self)
        btn.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        btn.setIcon(QIcon("resources/icons/plus-symbol-button.png"))
        
        btn.setFixedHeight(40)
        btn.setFixedWidth(40)
        title_layout.addWidget(btn)
        
        table_name = self.file_path.stem
        title_label = QLabel(f"Table: {TableContainerWidget.table_count}_{table_name}")
        title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        title_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        title_layout.addWidget(title_label)
        
        main_layout.addLayout(title_layout, 0, 0, 1, 2, QtCore.Qt.AlignmentFlag.AlignLeft)

        self.table = WorkspaceTable()
        main_layout.addWidget(self.table, 1, 0, 1, 2, QtCore.Qt.AlignmentFlag.AlignTop)

        self.setStyleSheet("""
            QWidget {
                background-color: rgb(31,31,31);
            }
            QLabel {
                padding: 1px;
                font-size: 16px; 
                font-weight: bold;
            }
        """)

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        btn.clicked.connect(self.open_import_options)
        self.signal_bus.update_options.connect(self.remove_option_from_selected)



    def open_import_options(self):
        self.import_dialog.optionsSelected.connect(self.set_selected_options)
        if self.import_dialog.exec():
            pass

    def set_selected_options(self, options: list):
        if options != self.selected_options:
            self.selected_options = options
            print("Selected options:", self.selected_options)
            self.load_data()

    def load_data(self):
        with open(f"src/instrument/data/{self.file_path}") as json_file:
            data = json.load(json_file)
            if data:
                self.insert_data(data)

    def remove_option_from_selected(self, label: str, row: int):
        if label in self.selected_options:
            self.selected_options.remove(label)
            self.import_dialog.uncheck_option(label)
            print(f"Option '{label}' removed from selected_options.")
            self.table.delete_row(row)


    def insert_data(self, data: dict):

        if "MeasurementJsonBuilder" in data and "Measurement Conditions" in data["MeasurementJsonBuilder"]:
            for key in data["MeasurementJsonBuilder"]["Measurement Conditions"]:
                if key in self.selected_options:
                    self.table.add_table_row(key, data["MeasurementJsonBuilder"]["Measurement Conditions"][key]["value"])

            for key in data:
                if key in self.selected_options:
                    self.table.add_table_row(key, data[key]["Spectral data"]["value"])

            for key in data["ColorimetricJsonBuilder"]["Colorimetric Data"]:
                if key in self.selected_options:
                    self.table.add_table_row(key, data["ColorimetricJsonBuilder"]["Colorimetric Data"][key]["value"])


class WorkspaceTable(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.signal_bus  = WorkspaceSignalBus().instance()

        self.setRowCount(0)
        self.setColumnCount(4)
        self.setHorizontalHeaderLabels(['', 'Key', 'Value', ''])
        self.verticalHeader().hide()
        self.setFixedHeight((self.rowCount()) * 40)

        self.setShowGrid(True)
        self.setGridStyle(QtCore.Qt.PenStyle.NoPen)
        self.setStyleSheet("""
                QTableWidget {
                    background-color: transparent;
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
        header.setStyleSheet("QHeaderView::section { height: 40px; }")
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

    def delete_row(self, row: int):
        print(row)
        self.removeRow(row)

    def add_table_row(self, label: str, value):
        for row in range(self.rowCount()):
            existing_label_item = self.item(row, 1)
            if existing_label_item and existing_label_item.text() == label:
                return

        bold_font = QFont()
        bold_font.setPointSize(12)
        bold_font.setBold(True)

        row_position = self.rowCount()
        self.insertRow(row_position)

        label_item = QTableWidgetItem(label)
        label_item.setFont(bold_font)
        self.setItem(row_position, 1, label_item)

        value_item = QTableWidgetItem(str(value))
        value_item.setFont(bold_font)
        self.setItem(row_position, 2, value_item)

        empty = QTableWidgetItem("")
        self.setItem(row_position, 3, empty)

        btn = QPushButton('', self)
        btn.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        btn.setIcon(QIcon("resources/icons/delete.png"))
        btn.setFixedWidth(40)
        self.setCellWidget(row_position, 0, btn)
        self.setRowHeight(row_position, 40)

        btn.setStyleSheet("""
            QPushButton {background-color: rgb(210,39,48);} 
        """)
        btn.clicked.connect(lambda _, lbl=label, rw=row_position: self.signal_bus.update_options.emit(lbl, rw))

        self.horizontalHeader().resizeSection(1, self.adjust_header_size() + 10)

        for row in range(self.rowCount()):
            if row % 2 == 0:
                self.change_row_background(row, QColor("#191919"))

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

class Workspace(QWidget):
    def __init__(self, workspace_name, parent=None):
        super().__init__(parent)
        self.ui = Ui_WorkspaceDesignForm()
        self.ui.setupUi(self)
        self.toast_msg_anchor = parent
        
        self.workspace_name = workspace_name
        self.explorer = self.ui.treeWidget
        self.grid = self.ui.gridLayout_5
        self.context_menu = CustomMenu(self)
        self.viewScalefactor = 1.15


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
    
    #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    def import_measurements_to_workspace_table(self):  
        dir = "src/instrument/data"  
        opened_file = open_dialog(self.toast_msg_anchor, direction=dir)
        
        if opened_file:
            file_path = Path(opened_file)
            container = QWidget()
            vbox_layout = QVBoxLayout(container)
            vbox_layout.setContentsMargins(0, 0, 0, 0)
            vbox_layout.setSpacing(0)

            table1 = TableContainerWidget(file_path)
            vbox_layout.addWidget(table1)
            self.ui.gridLayout_28.addWidget(container, TableContainerWidget.table_count, 0)
            self.ui.gridLayout_28.setAlignment(Qt.AlignmentFlag.AlignTop)
            table1.load_data_signal.emit()

            show_toast("Table Created", 3000, ToastType.SUCCESS, self.toast_msg_anchor)

        else:
            show_toast("No file selected", 3000, ToastType.ERROR, self.toast_msg_anchor)
    #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

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
        self.ui.widget_17.setStyleSheet("""QWidget {border: 0;}
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
        
        WORKSAPCE_DATA = {
        "workspace": self.workspace_name,
        "widgets": DATA }

        with open(f'{file_name}', 'w') as file:
            json.dump(WORKSAPCE_DATA, file, indent=4)
        
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
                
                if WIDGET.get('type') == 'SceneWidget':
                    widget = SpectralPlotWidget()
                    try:
                        widget.setObjectName(WIDGET.get('uniqe_name', 'DefaultID'))
                        widget.setSpectralData(WIDGET.get('data', ''))
                        
                        geometry = WIDGET.get('geometry', {})
                        x = geometry.get('x')
                        y = geometry.get('y')
                        width = geometry.get('width')
                        height = geometry.get('height')

                        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)) or not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
                            raise ValueError(f"Invalid geometry values")

                        widget.setGeometryProperties(x, y, width, height)
                        
                        self.scene.addWidget(widget)
                    except Exception as widget_error:
                        # show_toast(f"Error processing widget: \n{widget_error}", 3000, ToastType.ERROR)
                        pass
            
            self.update_explorer()

        except FileNotFoundError as fnf_error:
            pass
        except json.JSONDecodeError:
            pass
        except ValueError as ve:
            pass
        except Exception as e:
            pass

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