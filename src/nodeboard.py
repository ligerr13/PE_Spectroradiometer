from PyQt6.QtCore import QObject, QLineF
from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QWidget
from PyQt6.QtGui import QColor, qRgb
from functools import partial
from src.objects.workspace_1 import Ui_Form

class CustomWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Set up the UI from the generated file
        self.ui = Ui_Form()
        self.ui.setupUi(self)

class NodeBoard(QObject):
    def __init__(self, resource):
        super().__init__()
        self.ui = resource
        self.prev_button = None
        self.grid = self.ui.gridLayout_4

        self.test_widget = CustomWidget()
        self.test_widget2 = CustomWidget()

        self.view = self.ui.graphicsView
        self.scene = QGraphicsScene()

        #Calling Methods
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
            self.scene.addLine(vLine, red)

        while hor < hLines:
            hor = hor + 1
            hLine = QLineF(leftX, leftY, rightX, rightY)
            leftY, rightY = leftY + side, rightY + side
            self.scene.addLine(hLine, blue)

        grid.addWidget(self.view, 1, 1, 1, 1)