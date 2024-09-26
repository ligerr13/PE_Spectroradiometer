# Form implementation generated from reading ui file '.\src\ui\resource.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from importlib.resources import path
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        MainWindow.resize(1507, 934)
        MainWindow.setMinimumSize(QtCore.QSize(832, 624))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.ActionsContextMenu)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\src\\ui\\../../resources/icons/prism.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow {background-color: rgb(31, 31, 31);border-top: 1px solid rgba(129,129,129,50);}\n"
"\n"
"QPushButton {\n"
"        border: 0px;\n"
"        }\n"
"QPushButton:hover {\n"
"            background: rgb(55, 55, 55);\n"
"        }\n"
"QPushButton:checked  {\n"
"        border: 0px;\n"
"        background-color: rgb(63, 101, 255);\n"
"}")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("border: 0px;")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(40, 40))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.tabWidget.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.tabWidget.setStyleSheet("QTabWidget\n"
"{\n"
"      background: rgb(51, 51, 51);\n"
"}\n"
"QTabWidget::pane {\n"
"    border-top: 1px solid rgba(129,129,129,50);\n"
"    top: 1px;\n"
"} \n"
"\n"
"QTabBar::tab {\n"
"    color: grey;\n"
"    padding: 15 0 15 15;\n"
"    font: 700 10pt \"Consolas\";\n"
"    border: 2px;\n"
"    /*border-top-right-radius: 1px;*/\n"
"    border-left: 1px solid rgba(129, 129, 129, 50);\n"
"} \n"
"\n"
"QTabBar::tab:selected { \n"
"    background-color: rgb(45, 45, 45);\n"
"    border-bottom: 2px solid   rgb(0, 150, 255);\n"
"    /*border-bottom: 1px solid rgb(31,31,31);*/\n"
"    color: white;\n"
"}\n"
"QTabBar::tab:selected:hover{\n"
"    background-color: rgb(45, 45, 45);\n"
"}\n"
"QTabBar::tab:hover { \n"
"      background: rgb(45, 45, 45);\n"
"}\n"
"QTabWidget::tab-bar  {\n"
"left: 54px;\n"
"top: 1px;\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.home = QtWidgets.QWidget()
        self.home.setStyleSheet("background: rgb(20, 20, 20);")
        self.home.setObjectName("home")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.home)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(parent=self.home)
        self.widget.setMinimumSize(QtCore.QSize(60, 0))
        self.widget.setMaximumSize(QtCore.QSize(18, 16777215))
        self.widget.setStyleSheet("background-color: rgb(51, 51, 51);border-radius: 5px;")
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_3 = QtWidgets.QWidget(parent=self.widget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.line_3 = QtWidgets.QFrame(parent=self.widget_3)
        self.line_3.setStyleSheet("background-color: rgba(129, 129, 129, 50);\n"
"border: 0px;\n"
"border-radius: 50%")
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)
        spacerItem = QtWidgets.QSpacerItem(20, 411, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.line = QtWidgets.QFrame(parent=self.widget_3)
        self.line.setStyleSheet("background-color: rgba(129, 129, 129, 50);\n"
"border: 0px;\n"
"border-radius: 50%")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\src\\ui\\../../resources/icons/play-button-arrowhead.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_13.setIcon(icon1)
        self.pushButton_13.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_4.addWidget(self.pushButton_13)
        self.toolButton_2 = QtWidgets.QToolButton(parent=self.widget_3)
        self.toolButton_2.setMinimumSize(QtCore.QSize(0, 35))
        self.toolButton_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.toolButton_2.setStyleSheet("QToolButton {\n"
"        border: 0px;\n"
"         background: rgb(55, 55, 55);\n"
"\n"
"        font: 700 10pt \"Segoe UI\";\n"
"        }\n"
"QToolButton:hover {\n"
"            background: rgb(75, 75, 75);\n"
"        }\n"
"QToolTip{ \n"
"        font: 12pt;\n"
"        color: rgb(100, 100, 100);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\src\\ui\\../../resources/icons/link.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_2.setIcon(icon2)
        self.toolButton_2.setIconSize(QtCore.QSize(15, 15))
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_2.setObjectName("toolButton_2")
        self.verticalLayout_4.addWidget(self.toolButton_2)
        self.verticalLayout_3.addWidget(self.widget_3)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\src\\ui\\../../resources/icons/home.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tabWidget.addTab(self.home, icon3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit_Aplication = QtGui.QAction(parent=MainWindow)
        self.actionExit_Aplication.setObjectName("actionExit_Aplication")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_13.clicked['bool'].connect(MainWindow.HandleMeasureDialog) # type: ignore
        self.toolButton_2.clicked.connect(MainWindow.HandleConnectionConfigDialog) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SpectroApp"))
        self.pushButton_13.setToolTip(_translate("MainWindow", "Measure"))
        self.toolButton_2.setToolTip(_translate("MainWindow", "None"))
        self.toolButton_2.setText(_translate("MainWindow", "  Connection status"))
        self.actionExit_Aplication.setText(_translate("MainWindow", "Exit Aplication"))

