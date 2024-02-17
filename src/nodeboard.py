from PyQt6.QtCore import QObject, QLineF
from PyQt6.QtWidgets import QGraphicsScene
from PyQt6.QtGui import QColor, qRgb
from functools import partial


class NodeBoard(QObject):
    def __init__(self, resource):
        super().__init__()
        self.ui = resource
        self.prev_button = None
        self.grid = self.ui.gridLayout_4

        #Calling Methods
        self.HandleButtonVisuals()




    def HandleButtonVisuals(self):
        for i, button in enumerate(self.ui.NodeBoardbuttonGroup.buttons()):
            button.clicked.connect(partial(self.handle_navbar_button_background_signal, button))           

    def handle_navbar_button_background_signal(self, button):
        if button == self.prev_button:
            self.prev_button.setStyleSheet("QPushButton {border: 0px;}QPushButton:hover {background: rgb(55, 55, 55);}")
            self.prev_button = None
        else:
            if self.prev_button is not None:
                self.prev_button.setStyleSheet("QPushButton {border: 0px;}QPushButton:hover {background: rgb(55, 55, 55);}")
            
            button.setStyleSheet("QPushButton {border: 0px;background-color: rgb(63, 101, 255);}, QPushButton:hover {background: rgb(55, 55, 55);}")
            self.prev_button = button

    def generateSquareTiles(self, grid):
        square = 60 
        scene = QGraphicsScene()
        view = self.ui.graphicsView
        view.setScene(scene)

        red = QColor(qRgb(50, 50, 50))
        blue = QColor(qRgb(70, 70, 70))
         # Set length of square's side and number of horizontal and vertical lines
        vLines = square
        hLines = square
        side = square/2
        # Set starting values for loops
        hor = 0
        ver = 0
        subdiv = square
        leftX,leftY = 0, 0
        rightX, rightY = subdiv*side, 0
        bottomX, bottomY= 0, 0
        topX, topY = 0, subdiv*side

        while ver < vLines:
        # Drawing vertical lines
            ver = ver + 1
            vLine = QLineF(bottomX, bottomY, topX, topY)
            bottomX, topX = bottomX + side, topX + side
            scene.addLine(vLine, red)

        while hor < hLines:
        #Drawing horizontal lines
            hor = hor + 1
            hLine = QLineF(leftX, leftY, rightX, rightY)
            leftY, rightY = leftY + side, rightY + side
            scene.addLine(hLine, blue)

        grid.addWidget(view, 1, 1, 1, 1)