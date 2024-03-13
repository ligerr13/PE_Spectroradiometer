# Form implementation generated from reading ui file 'ui/resource.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1178, 914)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(60, 0))
        self.widget.setMaximumSize(QtCore.QSize(18, 16777215))
        self.widget.setStyleSheet("background-color: rgb(45, 45, 45);\n"
"border-radius: 5px;")
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_3 = QtWidgets.QWidget(parent=self.widget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget_3)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(45, 16777215))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
"        border: 0px;\n"
"        font: 12pt;\n"
"        }\n"
"QPushButton:hover {\n"
"            background: rgb(55, 55, 55);\n"
"        }\n"
"QPushButton:checked  {\n"
"        border: 0px;\n"
"        background-color: rgb(63, 101, 255);\n"
"}\n"
"QToolTip{ \n"
"        font: 12pt;\n"
"        color: rgb(100, 100, 100);\n"
"}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/../../resources/icons/vector.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(True)
        self.pushButton.setObjectName("pushButton")
        self.NavBarbuttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.NavBarbuttonGroup.setObjectName("NavBarbuttonGroup")
        self.NavBarbuttonGroup.addButton(self.pushButton)
        self.verticalLayout_4.addWidget(self.pushButton)
        self.line_3 = QtWidgets.QFrame(parent=self.widget_3)
        self.line_3.setStyleSheet("background-color: rgba(129, 129, 129, 50);\n"
"border: 0px;\n"
"border-radius: 50%")
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget_3)
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_2.setMaximumSize(QtCore.QSize(45, 16777215))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"        border: 0px;\n"
"        font: 12pt;\n"
"        }\n"
"QPushButton:hover {\n"
"            background: rgb(55, 55, 55);\n"
"        }\n"
"QPushButton:checked  {\n"
"        border: 0px;\n"
"        background-color: rgb(63, 101, 255);\n"
"}\n"
"QToolTip{ \n"
"        font: 12pt;\n"
"        color: rgb(100, 100, 100);\n"
"}")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/../../resources/icons/workspace.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.NavBarbuttonGroup.addButton(self.pushButton_2)
        self.verticalLayout_4.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(20, 411, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.pushButton_13 = QtWidgets.QPushButton(parent=self.widget_3)
        self.pushButton_13.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_13.setMaximumSize(QtCore.QSize(45, 16777215))
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_13.setStyleSheet("QPushButton {\n"
"        border: 0px;\n"
"        font: 12pt;\n"
"        }\n"
"QPushButton:hover {\n"
"            background: rgb(55, 55, 55);\n"
"        }\n"
"QPushButton:checked  {\n"
"        border: 0px;\n"
"        background: rgb(55, 55, 55);\n"
"}\n"
"QToolTip{ \n"
"        font: 12pt;\n"
"        color: rgb(100, 100, 100);\n"
"}")
        self.pushButton_13.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui/../../resources/icons/play-button-arrowhead.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_13.setIcon(icon2)
        self.pushButton_13.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_4.addWidget(self.pushButton_13)
        self.line = QtWidgets.QFrame(parent=self.widget_3)
        self.line.setStyleSheet("background-color: rgba(129, 129, 129, 50);\n"
"border: 0px;\n"
"border-radius: 50%")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.widget_3)
        self.pushButton_3.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_3.setMaximumSize(QtCore.QSize(45, 16777215))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"        border: 0px;\n"
"        font: 12pt;\n"
"        }\n"
"QPushButton:hover {\n"
"            background: rgb(55, 55, 55);\n"
"        }\n"
"QPushButton:checked  {\n"
"        border: 0px;\n"
"        background-color: rgb(63, 101, 255);\n"
"}\n"
"QToolTip{ \n"
"        font: 12pt;\n"
"        color: rgb(100, 100, 100);\n"
"}")
        self.pushButton_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui/../../resources/icons/setting.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setChecked(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.NavBarbuttonGroup.addButton(self.pushButton_3)
        self.verticalLayout_4.addWidget(self.pushButton_3)
        self.verticalLayout_3.addWidget(self.widget_3)
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_2.setEnabled(True)
        self.widget_2.setMinimumSize(QtCore.QSize(495, 601))
        self.widget_2.setAutoFillBackground(False)
        self.widget_2.setStyleSheet("background-color: rgb(20, 20, 20); \n"
"border-radius: 5px;")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.widget_2)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 35))
        self.stackedWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.stackedWidget.setStyleSheet("border: 0px")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setToolTip("")
        self.page.setObjectName("page")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget_4 = QtWidgets.QWidget(parent=self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_4.setMaximumSize(QtCore.QSize(55, 250))
        self.widget_4.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton_10.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_10.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_10.setStyleSheet("QPushButton {\n"
"        border: 0px;\n"
"        font: 12pt;\n"
"        }\n"
"QPushButton:hover {\n"
"            background: rgb(55, 55, 55);\n"
"        }\n"
"QPushButton:checked  {\n"
"        border: 0px;\n"
"        background-color: rgb(63, 101, 255);\n"
"}\n"
"QToolTip{ \n"
"        font: 12pt;\n"
"        color: rgb(100, 100, 100);\n"
"}")
        self.pushButton_10.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ui/../../resources/icons/cursor.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_10.setIcon(icon4)
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setChecked(False)
        self.pushButton_10.setAutoExclusive(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.NodeBoardbuttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.NodeBoardbuttonGroup.setObjectName("NodeBoardbuttonGroup")
        self.NodeBoardbuttonGroup.addButton(self.pushButton_10)
        self.verticalLayout_6.addWidget(self.pushButton_10)
        self.line_7 = QtWidgets.QFrame(parent=self.widget_4)
        self.line_7.setStyleSheet("background-color: rgba(129, 129, 129, 50);\n"
"border: 0px;\n"
"border-radius: 50%;\n"
"margin: 5, 5, 5, 5;")
        self.line_7.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_6.addWidget(self.line_7)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton_4.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_4.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"        border: 0px;\n"
"        font: 12pt;\n"
"        }\n"
"QPushButton:hover {\n"
"            background: rgb(55, 55, 55);\n"
"        }\n"
"QPushButton:checked  {\n"
"        border: 0px;\n"
"        background-color: rgb(63, 101, 255);\n"
"}\n"
"QToolTip{ \n"
"        font: 12pt;\n"
"        color: rgb(100, 100, 100);\n"
"}")
        self.pushButton_4.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("ui/../../resources/icons/delete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon5)
        self.pushButton_4.setIconSize(QtCore.QSize(15, 15))
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setChecked(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.NodeBoardbuttonGroup.addButton(self.pushButton_4)
        self.verticalLayout_6.addWidget(self.pushButton_4)
        self.line_2 = QtWidgets.QFrame(parent=self.widget_4)
        self.line_2.setStyleSheet("background-color: rgba(129, 129, 129, 50);\n"
"border: 0px;\n"
"border-radius: 50%;\n"
"margin: 5, 5, 5, 5;")
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_6.addWidget(self.line_2)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton_5.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_5.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"        border: 0px;\n"
"        font: 12pt;\n"
"        }\n"
"QPushButton:hover {\n"
"            background: rgb(55, 55, 55);\n"
"        }\n"
"QPushButton:checked  {\n"
"        border: 0px;\n"
"        background-color: rgb(63, 101, 255);\n"
"}\n"
"QToolTip{ \n"
"        font: 12pt;\n"
"        color: rgb(100, 100, 100);\n"
"}")
        self.pushButton_5.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("ui/../../resources/icons/more.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_5.setIcon(icon6)
        self.pushButton_5.setIconSize(QtCore.QSize(15, 15))
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.NodeBoardbuttonGroup.addButton(self.pushButton_5)
        self.verticalLayout_6.addWidget(self.pushButton_5)
        self.line_4 = QtWidgets.QFrame(parent=self.widget_4)
        self.line_4.setStyleSheet("background-color: rgba(129, 129, 129, 50);\n"
"border: 0px;\n"
"border-radius: 50%;\n"
"margin: 5, 5, 5, 5;")
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_6.addWidget(self.line_4)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_6.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"        border: 0px;\n"
"        font: 12pt;\n"
"        }\n"
"QPushButton:hover {\n"
"            background: rgb(55, 55, 55);\n"
"        }\n"
"QPushButton:checked  {\n"
"        border: 0px;\n"
"        background-color: rgb(63, 101, 255);\n"
"}\n"
"QToolTip{ \n"
"        font: 12pt;\n"
"        color: rgb(100, 100, 100);\n"
"}")
        self.pushButton_6.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("ui/../../resources/icons/move.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_6.setIcon(icon7)
        self.pushButton_6.setIconSize(QtCore.QSize(15, 15))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setChecked(False)
        self.pushButton_6.setProperty("clickCounter", 0)
        self.pushButton_6.setObjectName("pushButton_6")
        self.NodeBoardbuttonGroup.addButton(self.pushButton_6)
        self.verticalLayout_6.addWidget(self.pushButton_6)
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton_11.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_11.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_11.setStyleSheet("QPushButton {\n"
"        border: 0px;\n"
"        font: 12pt;\n"
"        }\n"
"QPushButton:hover {\n"
"            background: rgb(55, 55, 55);\n"
"        }\n"
"QToolTip{ \n"
"        font: 12pt;\n"
"        color: rgb(100, 100, 100);\n"
"}")
        self.pushButton_11.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("ui/../../resources/icons/magnifying-glass-2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_11.setIcon(icon8)
        self.pushButton_11.setIconSize(QtCore.QSize(17, 17))
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_6.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton_12.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_12.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_12.setStyleSheet("QPushButton {\n"
"        border: 0px;\n"
"        font: 12pt;\n"
"        }\n"
"QPushButton:hover {\n"
"            background: rgb(55, 55, 55);\n"
"        }\n"
"QToolTip{ \n"
"        font: 12pt;\n"
"        color: rgb(100, 100, 100);\n"
"}")
        self.pushButton_12.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("ui/../../resources/icons/magnifying-glass.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_12.setIcon(icon9)
        self.pushButton_12.setIconSize(QtCore.QSize(17, 17))
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_6.addWidget(self.pushButton_12)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.gridLayout_4.addWidget(self.widget_4, 1, 0, 1, 1)
        self.widget_5 = QtWidgets.QWidget(parent=self.page)
        self.widget_5.setStyleSheet("color:white;\n"
"border-radius: 5px;\n"
"background-color: rgb(35, 35, 35);")
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_7.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_7.addItem(spacerItem1, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white")
        self.label_2.setObjectName("label_2")
        self.gridLayout_7.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.widget_5, 0, 1, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(parent=self.page)
        self.graphicsView.setStyleSheet("border:0px;\n"
"")
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.graphicsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.graphicsView.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.graphicsView.setResizeAnchor(QtWidgets.QGraphicsView.ViewportAnchor.NoAnchor)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_4.addWidget(self.graphicsView, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_9 = QtWidgets.QWidget(parent=self.page_4)
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.widget_11 = QtWidgets.QWidget(parent=self.widget_9)
        self.widget_11.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_11.setMaximumSize(QtCore.QSize(16777215, 45))
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.widget_11)
        self.pushButton_9.setMinimumSize(QtCore.QSize(60, 35))
        self.pushButton_9.setMaximumSize(QtCore.QSize(35, 16777215))
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_9.setStyleSheet("\n"
"QPushButton {\n"
"        border-radius: 5px;\n"
"        background-color: rgb(35, 35, 35);\n"
"        color: white;\n"
"        border: 0px\n"
"        }\n"
"QPushButton:hover {\n"
"            background: rgb(55, 55 55);\n"
"        }")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("ui/../../resources/icons/pencil.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_9.setIcon(icon10)
        self.pushButton_9.setIconSize(QtCore.QSize(15, 15))
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_4.addWidget(self.pushButton_9)
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.widget_11)
        self.pushButton_8.setMinimumSize(QtCore.QSize(75, 35))
        self.pushButton_8.setMaximumSize(QtCore.QSize(35, 16777215))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_8.setStyleSheet("\n"
"QPushButton {\n"
"        border-radius: 5px;\n"
"        background-color: rgb(35, 35, 35);\n"
"        color: white;\n"
"        border: 0px\n"
"        }\n"
"QPushButton:hover {\n"
"            background: rgb(220, 20, 60);\n"
"        }")
        self.pushButton_8.setIcon(icon5)
        self.pushButton_8.setIconSize(QtCore.QSize(15, 15))
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_4.addWidget(self.pushButton_8)
        self.verticalLayout_15.addWidget(self.widget_11)
        self.widget_10 = QtWidgets.QWidget(parent=self.widget_9)
        self.widget_10.setStyleSheet("")
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_15.addWidget(self.widget_10)
        self.gridLayout_3.addWidget(self.widget_9, 0, 2, 1, 1)
        self.line_5 = QtWidgets.QFrame(parent=self.page_4)
        self.line_5.setMaximumSize(QtCore.QSize(5, 16777215))
        self.line_5.setStyleSheet("background-color: rgba(129, 129, 129, 50);\n"
"border: 0px;\n"
"border-radius: 50%")
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_3.addWidget(self.line_5, 0, 1, 1, 1)
        self.widget_6 = QtWidgets.QWidget(parent=self.page_4)
        self.widget_6.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_7 = QtWidgets.QWidget(parent=self.widget_6)
        self.widget_7.setMaximumSize(QtCore.QSize(16777215, 130))
        self.widget_7.setObjectName("widget_7")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_7)
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QtCore.QSize(35, 35))
        self.pushButton_7.setMaximumSize(QtCore.QSize(1000, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_7.setStyleSheet("\n"
"QPushButton {\n"
"            border-radius: 5px;\n"
"            background-color: rgb(63, 101, 255);\n"
"            border:0px;\n"
"            color: white;\n"
"        }\n"
"QPushButton:hover {\n"
"                background: rgb(73, 111, 255);\n"
"        }")
        self.pushButton_7.setIcon(icon6)
        self.pushButton_7.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_5.addWidget(self.pushButton_7, 2, 0, 1, 3)
        self.toolButton = QtWidgets.QToolButton(parent=self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        self.toolButton.setMinimumSize(QtCore.QSize(35, 35))
        self.toolButton.setMaximumSize(QtCore.QSize(40, 40))
        self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.toolButton.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.toolButton.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.toolButton.setAcceptDrops(False)
        self.toolButton.setStyleSheet("QToolButton {\n"
"        background-color: rgb(45, 45, 45);\n"
"        border: 0px;\n"
"        }\n"
"QToolButton:hover {\n"
"            background: rgb(55, 55, 55);\n"
"        }")
        self.toolButton.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("ui/../../resources/icons/menu.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton.setIcon(icon11)
        self.toolButton.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.toolButton.setAutoRaise(True)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_5.addWidget(self.toolButton, 1, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget_7)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit.setBaseSize(QtCore.QSize(45, 45))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"color: white")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_5.addWidget(self.lineEdit, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(parent=self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(217, 217, 217);")
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.widget_7)
        self.line_6 = QtWidgets.QFrame(parent=self.widget_6)
        self.line_6.setStyleSheet("background-color: rgba(129, 129, 129, 50);\n"
"border: 0px;\n"
"border-radius: 50%")
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_7.addWidget(self.line_6)
        self.widget_8 = QtWidgets.QWidget(parent=self.widget_6)
        self.widget_8.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_9.setContentsMargins(-1, 9, -1, 9)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.widget_8)
        self.scrollArea.setStyleSheet("border: 0px;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_9.addWidget(self.scrollArea)
        self.verticalLayout_7.addWidget(self.widget_8)
        self.gridLayout_3.addWidget(self.widget_6, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.stackedWidget.addWidget(self.page_4)
        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_2, 1, 1, 1, 1)
        self.widget_12 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_13 = QtWidgets.QWidget(parent=self.widget_12)
        self.widget_13.setMinimumSize(QtCore.QSize(0, 25))
        self.widget_13.setStyleSheet("background-color: rgb(45, 45, 45);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.widget_13)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_2.addWidget(self.widget_13)
        self.gridLayout.addWidget(self.widget_12, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.NavBarbuttonGroup.idClicked['int'].connect(MainWindow.OnNavbarButtonClicked) # type: ignore
        self.pushButton_6.toggled['bool'].connect(MainWindow.HandleDragMode) # type: ignore
        self.pushButton_10.toggled['bool'].connect(MainWindow.HandleSelectMode) # type: ignore
        self.pushButton_4.toggled['bool'].connect(MainWindow.HandleDeleteMode) # type: ignore
        self.pushButton_5.toggled['bool'].connect(MainWindow.HandleCreateWidgetMode) # type: ignore
        self.pushButton_11.clicked.connect(MainWindow.HandleZoomIn) # type: ignore
        self.pushButton_12.clicked.connect(MainWindow.HandleZoomOut) # type: ignore
        self.pushButton_13.clicked['bool'].connect(MainWindow.HandleMeasureDialog) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setStyleSheet(_translate("MainWindow", "QPushButton {\n"
"        border: 0px;\n"
"        }\n"
"QPushButton:hover {\n"
"            background: rgb(55, 55, 55);\n"
"        }\n"
"QPushButton:checked  {\n"
"        border: 0px;\n"
"        background-color: rgb(63, 101, 255);\n"
"}"))
        self.pushButton.setToolTip(_translate("MainWindow", "Nodeboard"))
        self.pushButton_2.setToolTip(_translate("MainWindow", "Workspaces"))
        self.pushButton_13.setToolTip(_translate("MainWindow", "Measure"))
        self.pushButton_3.setToolTip(_translate("MainWindow", "Settings"))
        self.page.setStyleSheet(_translate("MainWindow", "QPushButton {\n"
"        border: 0px;\n"
"        }\n"
"QPushButton:hover {\n"
"            background: rgb(55, 55, 55);\n"
"        }"))
        self.pushButton_10.setToolTip(_translate("MainWindow", "Select:\n"
"Enable to select widgets."))
        self.pushButton_4.setToolTip(_translate("MainWindow", "Delete:\n"
"Click to delete the selected widget."))
        self.pushButton_5.setToolTip(_translate("MainWindow", "New:\n"
"Click to add a new widget."))
        self.pushButton_6.setToolTip(_translate("MainWindow", "Move:\n"
"Click to navigate within the scene"))
        self.pushButton_11.setToolTip(_translate("MainWindow", "Zoom in\n"
"Click here to zoom in."))
        self.pushButton_12.setToolTip(_translate("MainWindow", "Zoom out\n"
"Click here to zoom out."))
        self.label_2.setText(_translate("MainWindow", "Workspace: #991013A"))
        self.pushButton_9.setText(_translate("MainWindow", " Edit"))
        self.pushButton_8.setText(_translate("MainWindow", " Delete"))
        self.pushButton_7.setText(_translate("MainWindow", "  New Workspace"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", " Search Workplace"))
        self.label.setText(_translate("MainWindow", "My Workspaces"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
