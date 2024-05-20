from PyQt6.QtWidgets import QWidget, QGraphicsView, QGraphicsProxyWidget, QGraphicsScene, QMenu,QMenuBar, QGraphicsLineItem
from PyQt6.QtGui import QColor, qRgb, QTransform, QCursor
from PyQt6.QtCore import  QLineF, QPointF, QPoint, QSize, QObject

from src.objects.editSettingsContextMenu_1 import Ui_Form
from src.objects.workspaceDesignFomr_1 import Ui_WorkspaceDesignForm
from src.signals.signals import NodeBoardSignalBus
from src.dialogs.widgetCreatorDialog import WidgetCreatorDialog
from src.widgets.dataviewwidgetbase import DataViewTestWidget
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
        self.grid = self.ui.gridLayout_5
        self.context_menu = CustomMenu(self)
        self.viewScalefactor = 1.2
        # Need some config setup func or something 

        # Views and Scenes
        self.view = self.ui.graphicsView_2
        self.scene = NodeboardGraphicsScene()

        # Signal Bus
        self.signal_bus = signal_bus

        # Signals
        self.context_menu.cMenu.actionShow_Workspace_Grid.triggered.connect(self.handle_grid_visibility)
        self.scene.changed.connect(self._scene_changed)

        # QDialogs
        self.widgetCreator = WidgetCreatorDialog()
        self.textCreateToScene = TextToSceneDialog()

        # Calling Methods
        self.group_workspace_group_buttons_to_pages()
        self.view.setScene(self.scene)
        self.generate_grid_tiles_for_scene(self.grid)
        self.context_menu.setMinimumSize(self.context_menu.sizeHint())


    
    def _scene_changed(self):
        print(f"Scene changed in workspace: {self}")

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
        global_pos += QPoint(-195, 35)
        self.context_menu.exec(global_pos)
        self.ui.workspaceEditSettingsButton.clearFocus()
        
    def group_workspace_group_buttons_to_pages(self):
         for i, button in enumerate(self.ui.WorkspaceMenuButtonGroup.buttons()):
              self.ui.WorkspaceMenuButtonGroup.setId(button, i)
    #Not the most elegant way to solve this.. has to be a better way to change the style.
    def handle_left_menu_tab_visibility(self, state):
         self.ui.WorkspaceMenuWidget.setVisible(state)
         self.ui.widget_6.setStyleSheet("""QWidget {border: 0;}
                QPushButton {
                    font: 570 10pt "Consolas";
                    color: 	rgb(190, 190, 190);
                    padding: 5 5 0 5;
                     margin: 0 -1 0 0;
                    }
                QPushButton:hover {
                            color: white;
                        }
                QPushButton:checked  {
                        border: 0px;
                        border-radius: 0px;
                        border-bottom: 0px;
                        color: rgb(190, 190, 190);
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
            self.ui.widget_6.setStyleSheet("""QWidget {border: 0;}
                QPushButton {
                font: 570 10pt "Consolas";
                color: 	rgb(190, 190, 190);
                padding: 5 5 0 5;
                margin: 0 -1 0 0;
                }
                QPushButton:hover {
                            color: white;
                        }
                QPushButton:checked  {
                        border: 0px;
                        border-radius: 0px;
                        border-bottom: 3px solid  rgb(63, 101, 255);
                        color: white;
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
        colorH = QColor(qRgb(50, 50, 50))
        colorV = QColor(qRgb(70, 70, 70))
        vLines = 100
        hLines = 100
        side = 30
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


class NodeboardGraphicsScene(QGraphicsScene):
    def __init__(self, parent=None):
        QGraphicsScene.__init__(self, parent)

        # Signalbus
        self.nodeboard_signal_bus = NodeBoardSignalBus()

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

    def onDeselectWidget(self, deselected: QGraphicsProxyWidget):
        if isinstance(deselected, QGraphicsProxyWidget):
            deselected.widget().setStyleSheet("QWidget {\nbackground-color: rgb(45, 45, 45);\nborder-radius: 5px; }")
            self.selectedWidget = None

    def extract_widget_data(self):
        widget_data = []

        for item in self.items():
            if isinstance(item, QGraphicsProxyWidget):
                widget_item = item
                widget = widget_item.widget()

                if widget:
                    data = {
                        "type": type(widget).__name__,
                        "position": (widget_item.pos().x(), widget_item.pos().y()),
                        "spectral_data": widget.spectral_data if hasattr(widget, "spectral_data") else None
                    }
                    widget_data.append(data)

        return widget_data



        # # Hardcoded stuff for testing
        # self.spectral_test_widget = SpectralPlotWidget()
        # self.spectral_test_widget_2 = SpectralPlotWidget()
 
        # self.test_widget = CustomWidget()
        # self.test_widget2 = CustomWidget()
        # # self.spectral_data_2 = "7.9018e-4,7.8843e-4,7.8377e-4,7.7766e-4,7.5896e-4,7.1689e-4,6.6391e-4,6.2288e-4,6.0831e-4,6.2175e-4,6.4433e-4,6.6620e-4,6.7792e-4,6.8348e-4,6.9311e-4,7.0943e-4,7.2298e-4,7.3134e-4,7.3084e-4,7.2332e-4,7.1932e-4,7.2059e-4,7.2977e-4,7.3916e-4,7.4616e-4,7.5453e-4,7.6034e-4,7.6619e-4,7.7034e-4,7.7501e-4,7.7769e-4,7.7936e-4,7.8028e-4,7.7315e-4,7.5618e-4,7.2244e-4,6.7222e-4,6.2086e-4,5.8526e-4,5.8240e-4,6.0652e-4,6.3099e-4,6.4005e-4,6.2646e-4,6.1374e-4,6.1084e-4,6.1483e-4,6.1702e-4,6.1979e-4,6.2839e-4,6.4110e-4,6.6836e-4,7.0047e-4,7.2628e-4,7.4135e-4,7.4860e-4,7.5494e-4,7.6244e-4,7.7011e-4,7.7486e-4,7.8321e-4,7.9335e-4,7.9720e-4,8.0628e-4,8.1212e-4,8.1240e-4,8.1216e-4,8.1232e-4,8.1022e-4,8.0870e-4,8.0573e-4,8.0505e-4,8.0256e-4,7.9985e-4,7.9930e-4,7.9628e-4,7.8441e-4,7.2894e-4,6.1416e-4,4.6742e-4,3.4672e-4,2.9289e-4,2.9666e-4,3.1746e-4,3.6562e-4,4.4274e-4,5.2441e-4,5.9419e-4,6.4397e-4,6.7361e-4,6.9987e-4,7.1391e-4,7.2684e-4,7.3635e-4,7.4280e-4,7.4404e-4,7.4273e-4,7.4315e-4,7.4040e-4,7.3856e-4,7.3936e-4"
        # self.spectral_data = "1.0139e-4,1.0178e-4,1.0552e-4,1.0520e-4,1.1489e-4,1.2348e-4,1.4203e-4,1.5488e-4,1.6706e-4,1.8255e-4,2.0662e-4,2.3010e-4,2.3899e-4,2.4023e-4,2.5990e-4,2.9615e-4,3.2849e-4,3.7248e-4,4.3627e-4,5.0280e-4,5.8398e-4,6.4691e-4,6.9608e-4,7.3879e-4,7.7700e-4,8.1145e-4,8.4110e-4,8.8335e-4,9.2982e-4,9.7476e-4,1.0142e-3,1.0564e-3,1.0961e-3,1.1395e-3,1.1695e-3,1.1887e-3,1.2104e-3,1.2219e-3,1.2310e-3,1.2357e-3,1.2468e-3,1.2655e-3,1.2694e-3,1.2723e-3,1.2581e-3,1.2578e-3,1.2541e-3,1.2401e-3,1.2227e-3,1.1893e-3,1.1593e-3,1.1539e-3,1.1985e-3,1.2683e-3,1.3158e-3,1.3427e-3,1.3755e-3,1.4004e-3,1.3968e-3,1.3863e-3,1.4043e-3,1.4435e-3,1.4862e-3,1.5185e-3,1.5328e-3,1.5425e-3,1.5480e-3,1.5712e-3,1.6058e-3,1.6398e-3,1.6639e-3,1.6861e-3,1.6776e-3,1.6599e-3,1.6517e-3,1.6626e-3,1.6856e-3,1.7031e-3,1.7093e-3,1.7068e-3,1.7055e-3,1.7244e-3,1.7346e-3,1.7388e-3,1.7286e-3,1.7176e-3,1.7101e-3,1.7071e-3,1.7023e-3,1.7096e-3,1.7160e-3,1.7191e-3,1.7298e-3,1.7442e-3,1.7527e-3,1.7530e-3,1.7526e-3,1.7606e-3,1.7719e-3,1.7902e-3,1.7974e-3,1.8072e-3,1.7992e-3,1.7874e-3,1.7540e-3,1.7022e-3,1.6537e-3,1.6463e-3,1.6796e-3,1.7298e-3,1.7572e-3,1.7725e-3,1.7723e-3,1.7764e-3,1.7947e-3,1.8167e-3,1.8249e-3,1.8152e-3,1.8102e-3,1.7948e-3,1.7759e-3,1.7628e-3,1.7563e-3,1.7632e-3,1.7850e-3,1.8068e-3,1.8324e-3,1.8429e-3,1.8459e-3,1.8572e-3,1.8752e-3,1.8853e-3,1.8814e-3,1.8714e-3,1.8473e-3,1.8242e-3,1.7853e-3,1.7578e-3,1.7532e-3,1.7904e-3,1.8391e-3,1.8763e-3,1.8967e-3,1.9059e-3,1.9145e-3,1.9072e-3,1.8860e-3,1.8751e-3,1.8972e-3,1.9400e-3,1.9640e-3,1.9626e-3,1.9466e-3,1.9387e-3,1.9494e-3,1.9658e-3,1.9728e-3,1.9663e-3,1.9548e-3,1.9375e-3,1.9218e-3,1.9166e-3,1.9276e-3,1.9436e-3,1.9553e-3,1.9646e-3,1.9628e-3,1.9588e-3,1.9568e-3,1.9623e-3,1.9683e-3,1.9737e-3,1.9745e-3,1.9748e-3,1.9804e-3,1.9733e-3,1.9616e-3,1.9402e-3,1.9185e-3,1.9115e-3,1.9112e-3,1.9209e-3,1.9216e-3,1.9175e-3,1.9098e-3,1.8996e-3,1.8865e-3,1.8753e-3,1.8566e-3,1.8362e-3,1.8206e-3,1.8194e-3,1.8240e-3,1.8271e-3,1.8235e-3,1.8125e-3,1.8102e-3,1.8068e-3,1.8107e-3,1.8212e-3,1.8445e-3,1.8712e-3,1.8891e-3,1.9025e-3,1.8962e-3,1.8795e-3,1.8507e-3,1.8011e-3,1.7328e-3,1.6763e-3,1.6598e-3,1.6754e-3,1.6973e-3,1.7087e-3,1.7150e-3,1.7214e-3,1.7298e-3,1.7442e-3,1.7498e-3,1.7559e-3,1.7631e-3,1.7673e-3,1.7747e-3,1.7881e-3,1.8000e-3,1.8039e-3,1.8001e-3,1.7933e-3,1.7865e-3,1.7803e-3,1.7776e-3,1.7740e-3,1.7685e-3,1.7559e-3,1.7421e-3,1.7291e-3,1.7211e-3,1.7227e-3,1.7319e-3,1.7400e-3,1.7443e-3,1.7354e-3,1.7189e-3,1.7042e-3,1.6870e-3,1.6693e-3,1.6456e-3,1.6212e-3,1.6046e-3,1.5995e-3,1.6023e-3,1.6155e-3,1.6278e-3,1.6379e-3,1.6501e-3,1.6597e-3,1.6723e-3,1.6800e-3,1.6834e-3,1.6802e-3,1.6742e-3,1.6705e-3,1.6695e-3,1.6684e-3,1.6551e-3,1.6283e-3,1.5943e-3,1.5627e-3,1.5456e-3,1.5491e-3,1.5561e-3,1.5698e-3,1.5751e-3,1.5654e-3,1.5314e-3,1.4877e-3,1.4726e-3,1.4922e-3,1.5365e-3,1.5815e-3,1.6070e-3,1.6229e-3,1.6319e-3,1.6309e-3,1.6319e-3,1.6281e-3,1.6274e-3,1.6254e-3,1.6226e-3,1.6177e-3,1.6101e-3,1.6066e-3,1.6028e-3,1.5979e-3,1.5946e-3,1.5983e-3,1.5940e-3,1.5907e-3,1.5869e-3,1.5839e-3,1.5791e-3,1.5703e-3,1.5644e-3,1.5531e-3,1.5111e-3,1.4272e-3,1.3209e-3,1.2289e-3,1.1972e-3,1.2220e-3,1.2509e-3,1.2663e-3,1.2863e-3,1.3074e-3,1.3215e-3,1.3537e-3,1.3897e-3,1.4073e-3,1.4015e-3,1.3819e-3,1.3710e-3,1.3754e-3,1.3928e-3,1.4174e-3,1.4360e-3,1.4537e-3,1.4720e-3,1.4825e-3,1.4942e-3,1.5037e-3,1.5129e-3,1.5142e-3,1.5119e-3,1.4982e-3,1.4585e-3,1.3696e-3,1.2484e-3,1.1263e-3,1.0415e-3,1.0336e-3,1.0839e-3,1.1435e-3,1.1632e-3,1.1340e-3,1.1009e-3,1.0884e-3,1.0942e-3,1.1021e-3,1.1095e-3,1.1244e-3,1.1534e-3,1.2190e-3,1.2940e-3,1.3596e-3,1.3982e-3,1.4145e-3,1.4302e-3,1.4462e-3,1.4749e-3,1.4992e-3,1.5145e-3,1.5427e-3,1.5675e-3,1.5869e-3,1.5937e-3,1.6026e-3,1.6141e-3,1.6154e-3,1.6110e-3,1.6022e-3,1.5979e-3,1.5929e-3,1.5888e-3,1.5906e-3,1.5865e-3,1.5767e-3,1.5531e-3,1.4488e-3,1.2273e-3,9.3450e-4,6.9164e-4,5.7825e-4,5.7702e-4,6.1497e-4,7.0560e-4,8.4966e-4,1.0050e-3,1.1418e-3,1.2484e-3,1.3165e-3,1.3693e-3,1.4097e-3,1.4296e-3,1.4467e-3,1.4599e-3,1.4650e-3,1.4671e-3,1.4648e-3,1.4577e-3,1.4529e-3,1.4507e-3"
        
        
        # self.spectral_test_widget.set_spectral_data(self.spectral_data)
        # # self.spectral_test_widget_2.set_spectral_data(self.spectral_data)


        # # self.scene.addWidget(self.test_widget)
        # self.scene.addWidget(self.spectral_test_widget).setPos(QPointF(400.0, 0.0))
        # # self.scene.addWidget(self.spectral_test_widget).setPos(QPointF(50.0, 100.0))