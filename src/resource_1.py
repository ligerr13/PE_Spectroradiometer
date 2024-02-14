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
        MainWindow.resize(850, 741)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setStyleSheet("background-color: rgba(129, 129, 129, 50);\n"
"border: 0px;\n"
"border-radius: 50%")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 1, 1, 1)
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
        self.pushButton.setStyleSheet("border: 0px")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/../../resources/icons/vector.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
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
        self.pushButton_2.setStyleSheet("border: 0px")
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
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.widget_3)
        self.pushButton_3.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_3.setMaximumSize(QtCore.QSize(45, 16777215))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet("border: 0px")
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui/../../resources/icons/setting.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setChecked(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.NavBarbuttonGroup.addButton(self.pushButton_3)
        self.verticalLayout_4.addWidget(self.pushButton_3)
        self.verticalLayout_3.addWidget(self.widget_3)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
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
        self.stackedWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
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
        self.widget_4.setMaximumSize(QtCore.QSize(50, 105))
        self.widget_4.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton_4.setMinimumSize(QtCore.QSize(35, 35))
        self.pushButton_4.setMaximumSize(QtCore.QSize(35, 35))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setStyleSheet("border: 0px\n"
"")
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui/../../resources/icons/delete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(15, 15))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_6.addWidget(self.pushButton_4)
        self.line_2 = QtWidgets.QFrame(parent=self.widget_4)
        self.line_2.setStyleSheet("background-color: rgba(129, 129, 129, 50);\n"
"border: 0px;\n"
"border-radius: 50%")
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_6.addWidget(self.line_2)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton_6.setMinimumSize(QtCore.QSize(35, 35))
        self.pushButton_6.setMaximumSize(QtCore.QSize(35, 35))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_6.setStyleSheet("border: 0px\n"
"")
        self.pushButton_6.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ui/../../resources/icons/move.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QtCore.QSize(15, 15))
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_6.addWidget(self.pushButton_6)
        self.line_4 = QtWidgets.QFrame(parent=self.widget_4)
        self.line_4.setStyleSheet("background-color: rgba(129, 129, 129, 50);\n"
"border: 0px;\n"
"border-radius: 50%")
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_6.addWidget(self.line_4)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton_5.setMinimumSize(QtCore.QSize(35, 35))
        self.pushButton_5.setMaximumSize(QtCore.QSize(35, 35))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_5.setStyleSheet("border: 0px\n"
"")
        self.pushButton_5.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("ui/../../resources/icons/more.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_5.setIcon(icon5)
        self.pushButton_5.setIconSize(QtCore.QSize(15, 15))
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_6.addWidget(self.pushButton_5)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.gridLayout_4.addWidget(self.widget_4, 1, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(parent=self.page)
        self.graphicsView.setStyleSheet("border:0px;\n"
"")
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
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.widget_11)
        self.pushButton_9.setMinimumSize(QtCore.QSize(60, 35))
        self.pushButton_9.setMaximumSize(QtCore.QSize(35, 16777215))
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_9.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(35, 35, 35);\n"
"color: white;\n"
"border: 0px")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("ui/../../resources/icons/pencil.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_9.setIcon(icon6)
        self.pushButton_9.setIconSize(QtCore.QSize(15, 15))
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_4.addWidget(self.pushButton_9)
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.widget_11)
        self.pushButton_8.setMinimumSize(QtCore.QSize(75, 35))
        self.pushButton_8.setMaximumSize(QtCore.QSize(35, 16777215))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_8.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(35, 35, 35);\n"
"color: white;\n"
"border: 0px")
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setIconSize(QtCore.QSize(15, 15))
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_4.addWidget(self.pushButton_8)
        self.verticalLayout_15.addWidget(self.widget_11)
        self.widget_10 = QtWidgets.QWidget(parent=self.widget_9)
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
        self.widget_7.setMaximumSize(QtCore.QSize(16777215, 55))
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget_7)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit.setBaseSize(QtCore.QSize(45, 45))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("background-color: rgb(45, 45, 45);\n"
"border-radius: 5px;")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.toolButton = QtWidgets.QToolButton(parent=self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        self.toolButton.setMinimumSize(QtCore.QSize(35, 0))
        self.toolButton.setMaximumSize(QtCore.QSize(40, 40))
        self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.toolButton.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.toolButton.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.toolButton.setAcceptDrops(False)
        self.toolButton.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(35, 35, 35);\n"
"color: white;\n"
"border: 0px")
        self.toolButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("ui/../../resources/icons/menu.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton.setIcon(icon7)
        self.toolButton.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.toolButton.setAutoRaise(True)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_3.addWidget(self.toolButton)
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QtCore.QSize(35, 35))
        self.pushButton_7.setMaximumSize(QtCore.QSize(35, 35))
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_7.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(63, 101, 255);\n"
"border:0px;")
        self.pushButton_7.setText("")
        self.pushButton_7.setIcon(icon5)
        self.pushButton_7.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_3.addWidget(self.pushButton_7)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 282, 600))
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
        self.gridLayout.addWidget(self.widget_2, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.NavBarbuttonGroup.idClicked['int'].connect(MainWindow.OnNavbarButtonClicked) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_9.setText(_translate("MainWindow", " Edit"))
        self.pushButton_8.setText(_translate("MainWindow", " Delete"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", " Search Workplace"))
