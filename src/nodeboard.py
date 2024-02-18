from PyQt6.QtCore import QObject, QLineF, QPointF, pyqtSignal
from PyQt6.QtWidgets import QGraphicsScene, QWidget, QGraphicsProxyWidget
from PyQt6.QtGui import QColor, qRgb, QTransform
from src.objects.workspace_1 import Ui_Form
from src.signals.nodeboardsignalbus import NodeBoardSignalBus


class NodeboardGraphicsScene(QGraphicsScene):
    def __init__(self, parent=None):
        QGraphicsScene.__init__(self, parent)
        # Signalbus
        self.nodeboard_signal_bus = NodeBoardSignalBus()

        # Buttons
        self.SelectButton = None
        self.DeleteButton = None

        # Widgets
        self.selectedWidget = None

        # Signals and Methods
        self.nodeboard_signal_bus.widgetSelectedSignal.connect(self.onSelectWidget)
        self.nodeboard_signal_bus.widgetDeselectedSignal.connect(self.onDeselectWidget)
        self.nodeboard_signal_bus.widgetDeletedSignal.connect(self.onWidgetDelete)

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



#Test CustomWidget
class CustomWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        
        #Setup UI
        self.ui = Ui_Form()
        self.ui.setupUi(self)

class NodeBoard(QObject):

    def __init__(self, resource):
        super().__init__()
        
        # Setup UI
        self.ui = resource
        self.grid = self.ui.gridLayout_4

        # Hardcoded stuff for testing
        self.test_widget = CustomWidget()
        self.test_widget2 = CustomWidget()

        #Views and Scenes
        self.view = self.ui.graphicsView
        self.scene = NodeboardGraphicsScene()

        # Calling Methods
        self.view.setScene(self.scene)
        self.scene.addWidget(self.test_widget)
        self.scene.addWidget(self.test_widget2).setPos(QPointF(0.0, 100.0))

  

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

        grid.addWidget(self.view, 1, 1, 1, 1)