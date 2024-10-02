from PyQt6.QtWidgets import QWidget, QSplitterHandle,QGraphicsView, QGraphicsProxyWidget, QGraphicsScene, QMenu, QGraphicsLineItem, QTreeWidgetItem, QPushButton
from PyQt6.QtGui import QColor, qRgb, QTransform, QCursor, QStandardItem
from PyQt6.QtCore import  Qt, QLineF, QPointF, QPoint, QSize, QObject, Qt, pyqtSignal, pyqtSlot
from PyQt6 import QtCore
import json

from src.objects.editSettingsContextMenu import Ui_Form
from src.objects.workspaceDesignFomr import Ui_WorkspaceDesignForm
from src.signals.signals import NodeBoardSignalBus
from src.dialogs.widgetCreatorDialog import WidgetCreatorDialog
from src.widgets.testwidgetbase import CustomWidget
from src.widgets.spectralplottest import SpectralPlotWidget
from src.signals.signals import WorkspaceSignalBus
from src.dialogs.textToSceneDialog import TextToSceneDialog

from src.globals.utils import open_dialog


from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QSplitter, QLabel, QTableWidget, QTableWidgetItem
)
from src.globals.utils import show_toast, ToastType


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
        
        # Need some config setup func or something 
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
    
    def import_measurements_to_workspace_table(self):
        show_toast("Opening Stuff", 3000, ToastType.SUCCESS, self.toast_msg_anchor)
        open_dialog(self.toast_msg_anchor, direction = "src/instrument/data")
        pass

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