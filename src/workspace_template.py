from PyQt6.QtWidgets import QWidget, QGraphicsView, QGraphicsProxyWidget, QGraphicsScene, QMenu, QGraphicsLineItem, QTreeWidgetItem, QPushButton
from PyQt6.QtGui import QColor, qRgb, QTransform, QCursor, QStandardItem
from PyQt6.QtCore import  QLineF, QPointF, QPoint, QSize, QObject, Qt
from PyQt6 import QtCore

from src.objects.editSettingsContextMenu import Ui_Form
from src.objects.workspaceDesignFomr import Ui_WorkspaceDesignForm
from src.signals.signals import NodeBoardSignalBus
from src.dialogs.widgetCreatorDialog import WidgetCreatorDialog
from src.widgets.testwidgetbase import CustomWidget
from src.widgets.spectralplottest import SpectralPlotWidget
from src.signals.signals import WorkspaceSignalBus
from src.dialogs.textToSceneDialog import TextToSceneDialog



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
    def __init__(self, signal_bus, parent=None):
        super().__init__(parent)
        self.ui = Ui_WorkspaceDesignForm()
        self.ui.setupUi(self)

        self.explorer = self.ui.treeWidget
        self.grid = self.ui.gridLayout_5
        self.context_menu = CustomMenu(self)
        self.viewScalefactor = 1.15
        
        # Need some config setup func or something 

        # Views and Scenes
        self.view = self.ui.graphicsView_2
        self.scene = NodeboardGraphicsScene()
        self.button = QPushButton(parent=self.view, text="asd")

        # Signal Bus
        # self.signal_bus = signal_bus
        self.signal_bus =  WorkspaceSignalBus.instance()


        # Signals
        self.context_menu.cMenu.actionShow_Workspace_Grid.triggered.connect(self.handle_grid_visibility)
        self.scene.changed.connect(self._scene_changed)
        self.signal_bus.widgetDataToPorpertyEditor.connect(self.update_properties_panel_date)

        # QDialogs
        self.widgetCreator = WidgetCreatorDialog()
        self.textCreateToScene = TextToSceneDialog()


        # Hardcoded stuff for testing
        self.spectral_test_widget = SpectralPlotWidget()
        self.spectral_test_widget_2 = SpectralPlotWidget()
        self.spectral_test_widget.setObjectName("Sajtos Widget")
        self.spectral_test_widget_2.setObjectName("Kekszes Widget")
        self.spectral_test_widget.setGeometryProperties(30,40,230,230)
        self.spectral_test_widget_2.setGeometryProperties(30,275,350,350)
        self.spectral_data = "1.0139e-4,1.0178e-4,1.0552e-4,1.0520e-4,1.1489e-4,1.2348e-4,1.4203e-4,1.5488e-4,1.6706e-4,1.8255e-4,2.0662e-4,2.3010e-4,2.3899e-4,2.4023e-4,2.5990e-4,2.9615e-4,3.2849e-4,3.7248e-4,4.3627e-4,5.0280e-4,5.8398e-4,6.4691e-4,6.9608e-4,7.3879e-4,7.7700e-4,8.1145e-4,8.4110e-4,8.8335e-4,9.2982e-4,9.7476e-4,1.0142e-3,1.0564e-3,1.0961e-3,1.1395e-3,1.1695e-3,1.1887e-3,1.2104e-3,1.2219e-3,1.2310e-3,1.2357e-3,1.2468e-3,1.2655e-3,1.2694e-3,1.2723e-3,1.2581e-3,1.2578e-3,1.2541e-3,1.2401e-3,1.2227e-3,1.1893e-3,1.1593e-3,1.1539e-3,1.1985e-3,1.2683e-3,1.3158e-3,1.3427e-3,1.3755e-3"
        self.spectral_data_2 = "1.0139e-4,1.0178e-4,1.0552e-4,1.0520e-4,1.1489e-4,1.2348e-4,1.4203e-4,1.5488e-4,1.6706e-4"
        self.spectral_test_widget.setSpectralData(self.spectral_data_2)
        self.spectral_test_widget_2.setSpectralData(self.spectral_data)
        self.scene.addWidget(self.spectral_test_widget)
        self.scene.addWidget(self.spectral_test_widget_2)


        # Calling Methods
        self.group_workspace_group_buttons_to_pages()
        self.view.setScene(self.scene)
        self.generate_grid_tiles_for_scene(self.grid)
        self.context_menu.setMinimumSize(self.context_menu.sizeHint())
        self.handle_menu_widget_visibility(True)
        self.handle_left_menu_tab_visibility(False)
        self.handle_properties_widget_visibility(False)
        self.update_explorer() #Should be called when the scene changes

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
        # print(f"{self.view.viewport().width()}x{self.view.viewport().height()}") 
    
    #Prototype update_explorer
    def update_explorer(self):
        widget_items = self.explorer.findItems("Widget", Qt.MatchFlag.MatchExactly | Qt.MatchFlag.MatchRecursive)
        
        if widget_items:
            for item in widget_items:
                widget_data = self.scene.extract_widget_data()

                for objName in widget_data:
                    item.addChild(QTreeWidgetItem([objName]))

    def _scene_changed(self): #This one called too many times, something isnt working the way i thought.
        # print(f"Scene changed in workspace: {self.objectName()}")
        pass

    def handle_grid_visibility(self, state):
        if not state:
            for gridLines in self.scene.items():
                if isinstance(gridLines, QGraphicsLineItem):
                    self.scene.removeItem(gridLines)
        else:
            self.generate_grid_tiles_for_scene(self.grid)
        
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
            if selected is not None:
                if  selected == False:
                    self.view.setDragMode(QGraphicsView.DragMode.NoDrag)
                else:
                    self.view.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)

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
        leftX,leftY = 0, 0
        rightX, rightY = subdiv*side, 0
        bottomX, bottomY= 0, 0
        topX, topY = 0, subdiv*side

        while ver < vLines:
            ver = ver + 1
            vLine = QLineF(bottomX, bottomY, topX, topY)
            bottomX, topX = bottomX + side, topX + side
            self.scene.addLine(vLine, colorH).setZValue(-1)

        while hor < hLines:
            hor = hor + 1
            hLine = QLineF(leftX, leftY, rightX, rightY)
            leftY, rightY = leftY + side, rightY + side
            self.scene.addLine(hLine, colorV).setZValue(-1)

        grid.addWidget(self.view, 0, 1, 1, 1)

    def handle_add_text_to_scene(self):
        print("Opening text dialog or widget...")
        self.textCreateToScene.popUp()
    
    def handle_add_image_to_scene(self):
        print("Opening image dialog or widget...")

    def update_properties_panel_date(self, property_holder):
        #FOR TESTING ITS FINE FOR NOW
        self.ui.lineEdit_7.setText(str(property_holder.objectName))
        self.ui.x_lineEdit.setText(str(property_holder.x))
        self.ui.y_lineEdit.setText(str(property_holder.y))
        self.ui.lineEdit.setText(str(property_holder.width))
        self.ui.lineEdit_2.setText(str(property_holder.height))
        self.ui.lineEdit_3.setText(str(property_holder.minimumWidth))
        self.ui.lineEdit_4.setText(str(property_holder.minimumHeight))
        self.ui.lineEdit_6.setText(str(property_holder.maximumWidth))
        self.ui.lineEdit_5.setText(str(property_holder.maximumHeight))

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
    
    # Overwriten mousePressEvent
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

    # Connected Methods
    def onWidgetDelete(self, deleted: QGraphicsProxyWidget):
        if isinstance(deleted, QGraphicsProxyWidget):
                self.nodeboard_signal_bus.onWidgetDeselectedSignalEmit(deleted)
                self.removeItem(deleted)

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
                    widget_data.append(widget.objectName)

        return widget_data