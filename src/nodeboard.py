from PyQt6.QtCore import QObject, QLineF
from PyQt6.QtWidgets import QGraphicsScene, QGridLayout
from PyQt6.QtGui import QColor, qRgb

class NodeBoard(QObject):
    def __init__(self, resource):
        super().__init__()
        self.ui = resource

        self.prev_button = None
        self.grid = self.ui.gridLayout_4

        #Signals and Connections
        self.ui.pushButton_4.clicked.connect(lambda: self.handle_navbar_button_background_signal(self.ui.pushButton_4))

        self.ui.pushButton_5.clicked.connect(lambda: self.handle_navbar_button_background_signal(self.ui.pushButton_5))

        self.ui.pushButton_6.clicked.connect(lambda: self.handle_navbar_button_background_signal(self.ui.pushButton_6))



    def handle_navbar_button_background_signal(self, button):
        if button == self.prev_button:
            self.prev_button.setStyleSheet("border: 0px")
            self.prev_button = None
        else:
            if self.prev_button is not None:
                self.prev_button.setStyleSheet("border: 0px")
            
            button.setStyleSheet("background-color: rgba(0, 0, 0, 50); border: 0px")
            self.prev_button = button

    def generateSquareTiles(self, grid):

        scene = QGraphicsScene()
        view = self.ui.graphicsView
        view.setScene(scene)

        red = QColor(qRgb(50, 50, 50))
        blue = QColor(qRgb(70, 70, 70))
                                            # Set length of square's side and number of horizontal and vertical lines
        vLines = 30
        hLines = 30
        side = 30
                                            # Set starting values for loops
        hor = 0
        ver = 0
        subdiv = 30
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