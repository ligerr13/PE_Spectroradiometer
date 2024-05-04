from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QGraphicsView, QGraphicsProxyWidget, QGraphicsScene, QTabBar
from PyQt6.QtGui import QColor, qRgb, QTransform
from PyQt6.QtCore import QObject, QLineF, QPointF, pyqtSignal


from src.objects.workspaceDesignFomr_1 import Ui_WorkspaceDesignForm
from src.signals.signals import NodeBoardSignalBus
from src.dialogs.widgetCreatorDialog import WidgetCreatorDialog
from src.widgets.dataviewwidgetbase import DataViewTestWidget
from src.widgets.testwidgetbase import CustomWidget
from src.widgets.spectralplottest import SpectralPlotWidget
from src.signals.signals import WorkspaceSignalBus

class WorkspaceDesignWidget(QWidget):
    def __init__(self, signal_bus, parent=None):
        super().__init__(parent)
        self.ui = Ui_WorkspaceDesignForm()
        self.ui.setupUi(self)
        self.grid = self.ui.gridLayout_5
        
        # Signal Bus
        self.signal_bus = signal_bus

        # Views and Scenes
        self.view = self.ui.graphicsView_2
        self.scene = NodeboardGraphicsScene()

        self.viewScalefactor = 1.2

        # QDialogs
        self.widgetCreator = WidgetCreatorDialog()


        # Hardcoded stuff for testing
        self.spectral_test_widget = SpectralPlotWidget()
        self.spectral_test_widget_2 = SpectralPlotWidget()
        self.test_widget = CustomWidget()
        self.test_widget2 = CustomWidget()
        self.spectral_data_2 = "7.9018e-4,7.8843e-4,7.8377e-4,7.7766e-4,7.5896e-4,7.1689e-4,6.6391e-4,6.2288e-4,6.0831e-4,6.2175e-4,6.4433e-4,6.6620e-4,6.7792e-4,6.8348e-4,6.9311e-4,7.0943e-4,7.2298e-4,7.3134e-4,7.3084e-4,7.2332e-4,7.1932e-4,7.2059e-4,7.2977e-4,7.3916e-4,7.4616e-4,7.5453e-4,7.6034e-4,7.6619e-4,7.7034e-4,7.7501e-4,7.7769e-4,7.7936e-4,7.8028e-4,7.7315e-4,7.5618e-4,7.2244e-4,6.7222e-4,6.2086e-4,5.8526e-4,5.8240e-4,6.0652e-4,6.3099e-4,6.4005e-4,6.2646e-4,6.1374e-4,6.1084e-4,6.1483e-4,6.1702e-4,6.1979e-4,6.2839e-4,6.4110e-4,6.6836e-4,7.0047e-4,7.2628e-4,7.4135e-4,7.4860e-4,7.5494e-4,7.6244e-4,7.7011e-4,7.7486e-4,7.8321e-4,7.9335e-4,7.9720e-4,8.0628e-4,8.1212e-4,8.1240e-4,8.1216e-4,8.1232e-4,8.1022e-4,8.0870e-4,8.0573e-4,8.0505e-4,8.0256e-4,7.9985e-4,7.9930e-4,7.9628e-4,7.8441e-4,7.2894e-4,6.1416e-4,4.6742e-4,3.4672e-4,2.9289e-4,2.9666e-4,3.1746e-4,3.6562e-4,4.4274e-4,5.2441e-4,5.9419e-4,6.4397e-4,6.7361e-4,6.9987e-4,7.1391e-4,7.2684e-4,7.3635e-4,7.4280e-4,7.4404e-4,7.4273e-4,7.4315e-4,7.4040e-4,7.3856e-4,7.3936e-4"
        self.spectral_data = "8.3521e-4,8.3311e-4,8.2984e-4,8.2244e-4,8.0330e-4,7.5898e-4,7.0482e-4,6.6052e-4,6.4606e-4,6.6024e-4,6.8321e-4,7.0359e-4,7.1511e-4,7.2468e-4,7.3507e-4,7.4769e-4,7.6474e-4,7.7228e-4,7.6982e-4,7.6444e-4,7.5931e-4,7.6102e-4,7.6856e-4,7.7924e-4,7.8693e-4,7.9462e-4,8.0052e-4,8.0443e-4,8.0908e-4,8.1353e-4,8.1735e-4,8.1876e-4,8.1815e-4,8.1244e-4,7.9444e-4,7.5805e-4,7.0704e-4,6.5281e-4,6.1598e-4,6.1319e-4,6.3630e-4,6.6445e-4,6.7230e-4,6.5922e-4,6.4472e-4,6.4074e-4,6.4402e-4,6.4668e-4,6.4991e-4,6.5855e-4,6.7462e-4,7.0181e-4,7.3238e-4,7.5895e-4,7.7453e-4,7.8277e-4,7.9113e-4,7.9632e-4,8.0440e-4,8.0618e-4,8.1825e-4,8.2497e-4,8.3365e-4,8.3960e-4,8.4500e-4,8.4786e-4,8.4794e-4,8.4627e-4,8.4814e-4,8.4000e-4,8.3799e-4,8.3919e-4,8.3666e-4,8.3402e-4,8.3356e-4,8.2895e-4,8.1697e-4,7.6156e-4,6.4026e-4,4.8672e-4,3.6437e-4,3.0921e-4,3.1460e-4,3.3508e-4,3.8465e-4,4.6412e-4,5.4860e-4,6.1854e-4,6.6936e-4,7.0452e-4,7.3056e-4,7.4617e-4,7.5815e-4,7.6667e-4,7.6939e-4,7.7237e-4,7.7534e-4,7.7484e-4,7.7319e-4,7.7301e-4,7.6837e-4"
        
        
        self.spectral_test_widget.set_spectral_data(self.spectral_data_2)
        self.spectral_test_widget_2.set_spectral_data(self.spectral_data)

        # Calling Methods
        self.groupWorkspaceGroupButtonsToPages()
        self.view.setScene(self.scene)
        self.generateSquareTiles(self.grid)
        self.scene.addWidget(self.test_widget)
        self.scene.addWidget(self.test_widget2).setPos(QPointF(400.0, 0.0))
        self.scene.addWidget(self.spectral_test_widget).setPos(QPointF(50.0, 100.0))
        self.scene.addWidget(self.spectral_test_widget_2).setPos(QPointF(650.0, 100.0))

        print(self.scene.extract_widget_data())
        
        
    def groupWorkspaceGroupButtonsToPages(self):
         for i, button in enumerate(self.ui.WorkspaceMenuButtonGroup.buttons()):
              print(button, i)
              self.ui.WorkspaceMenuButtonGroup.setId(button, i)

    def HandleMenuWidgetVisibility(self, state):
        if not self.ui.WorkspaceMenuWidget.isVisible():
            self.ui.WorkspaceMenuWidget.setVisible(state)
            

    def HandleCreateWidgetMode(self, selected: bool):
            if selected is not None:
                if  selected == False:
                    self.widgetCreator.closePopUp()
                else:
                    self.widgetCreator.popUp()
                    self.ui.CreateWidgetButton.setChecked(True)

    def HandleDragMode(self, selected: bool):
            if selected is not None:
                if  selected == False:
                    self.view.setDragMode(QGraphicsView.DragMode.NoDrag)
                else:
                    self.view.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)

    def HandleSelectMode(self, selected: bool):
            try:
                if selected is not None:
                    if selected == False:
                        self.scene.setSelecteButton(None)
                    else:
                        self.scene.setSelecteButton(self.sender())
            except AttributeError as e:
                print("An AttributeError occurred:", e)

    def HandleDeleteMode(self, selected: bool):
            if selected is not None:
                if  selected == False:
                    self.scene.setDeleteButton(None)
                else:
                    self.scene.setDeleteButton(self.sender())

    def HandleZoomIn(self):
            scale_tr = QTransform()
            scale_tr.scale(self.viewScalefactor, self.viewScalefactor)

            tr = self.view.transform() * scale_tr
            if tr.m11() <= 2.0 and tr.m22() <= 2.0:
                self.view.setTransform(tr)

    def HandleZoomOut(self):
            scale_tr = QTransform()
            scale_tr.scale(1 / self.viewScalefactor, 1 / self.viewScalefactor)

            tr = self.view.transform() * scale_tr
            if tr.m11() >= 0.4 and tr.m22() >= 0.4:
                self.view.setTransform(tr)

    
    def generateSquareTiles(self, grid):
        red = QColor(qRgb(50, 50, 50))
        blue = QColor(qRgb(70, 70, 70))
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
            self.scene.addLine(vLine, red).setZValue(-1)

        while hor < hLines:
            hor = hor + 1
            hLine = QLineF(leftX, leftY, rightX, rightY)
            leftY, rightY = leftY + side, rightY + side
            self.scene.addLine(hLine, blue).setZValue(-1)

        self.grid.addWidget(self.view, 0, 1, 1, 1)




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

        # Signals and Methods
        self.nodeboard_signal_bus.widgetSelectedSignal.connect(self.onSelectWidget)
        self.nodeboard_signal_bus.widgetDeselectedSignal.connect(self.onDeselectWidget)
        self.nodeboard_signal_bus.widgetDeletedSignal.connect(self.onWidgetDelete)

        #Calling methods
        print(self.extract_widget_data())

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
                # Más widget típusok kezelése hasonló módon

        return widget_data



