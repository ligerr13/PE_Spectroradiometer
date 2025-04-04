# Form implementation generated from reading ui file '.\src\ui\widget_creater_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(632, 590)
        Dialog.setStyleSheet("background-color: rgb(20, 20, 20); \n"
"border-radius: 0px;\n"
"    border: 0px;")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.page_selector_widget = QtWidgets.QWidget(parent=Dialog)
        self.page_selector_widget.setStyleSheet("background: rgb(20,20,20);")
        self.page_selector_widget.setObjectName("page_selector_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_selector_widget)
        self.horizontalLayout_2.setContentsMargins(5, 3, 0, 5)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.page_selector = QtWidgets.QWidget(parent=self.page_selector_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_selector.sizePolicy().hasHeightForWidth())
        self.page_selector.setSizePolicy(sizePolicy)
        self.page_selector.setMinimumSize(QtCore.QSize(200, 0))
        self.page_selector.setStyleSheet("QWidget {background: rgb(31,31,31); \n"
"border-top-left-radius: 2px; \n"
"border-bottom-left-radius: 2px; \n"
"border-right: 1px solid rgba(129, 129, 129,50);}\n"
"\n"
"QPushButton {\n"
"font: 570 10pt \"Consolas\";\n"
"color:     rgb(190, 190, 190);\n"
"margin: 0 0 0 0;\n"
"padding: 5,5,5,5;\n"
"border-radius: 2px;\n"
"border-right: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"            color: white;\n"
"            background:   rgb(40, 40, 40);\n"
"        }\n"
"QPushButton:checked  {\n"
"        border-left: 3px solid rgb(0, 150, 255);\n"
"        border-radius: 0px;\n"
"        color: white;\n"
"        background:  rgb(40, 40, 40);\n"
"}\n"
"QPushButton:unchecked  {\n"
"        border: 0px;\n"
"        background-color: transparent;\n"
"        color:     rgb(171, 171, 171);\n"
"}\n"
"QToolTip{ \n"
"        font: 12pt;\n"
"        color: rgb(100, 100, 100);\n"
"}")
        self.page_selector.setObjectName("page_selector")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_selector)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.custom_widget_button = QtWidgets.QPushButton(parent=self.page_selector)
        self.custom_widget_button.setMinimumSize(QtCore.QSize(60, 35))
        self.custom_widget_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.custom_widget_button.setStyleSheet("")
        self.custom_widget_button.setCheckable(True)
        self.custom_widget_button.setChecked(True)
        self.custom_widget_button.setObjectName("custom_widget_button")
        self.WidgetTypeGroup = QtWidgets.QButtonGroup(Dialog)
        self.WidgetTypeGroup.setObjectName("WidgetTypeGroup")
        self.WidgetTypeGroup.addButton(self.custom_widget_button)
        self.verticalLayout.addWidget(self.custom_widget_button)
        self.custom_widget_button_2 = QtWidgets.QPushButton(parent=self.page_selector)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.custom_widget_button_2.sizePolicy().hasHeightForWidth())
        self.custom_widget_button_2.setSizePolicy(sizePolicy)
        self.custom_widget_button_2.setMinimumSize(QtCore.QSize(60, 35))
        self.custom_widget_button_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.custom_widget_button_2.setCheckable(True)
        self.custom_widget_button_2.setObjectName("custom_widget_button_2")
        self.WidgetTypeGroup.addButton(self.custom_widget_button_2)
        self.verticalLayout.addWidget(self.custom_widget_button_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addWidget(self.page_selector)
        self.page_widget = QtWidgets.QWidget(parent=self.page_selector_widget)
        self.page_widget.setStyleSheet("    border: 0px;")
        self.page_widget.setObjectName("page_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_widget)
        self.verticalLayout_2.setContentsMargins(1, 1, 5, 5)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.page_widget)
        self.stackedWidget.setStyleSheet("border: 0px;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setStyleSheet("    border: 0px;")
        self.page.setObjectName("page")
        self.gridLayout = QtWidgets.QGridLayout(self.page)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.page)
        self.tabWidget.setStyleSheet("QTabWidget\n"
"{\n"
"    border: 0px;\n"
"      background: rgb(31,31,31);\n"
"}\n"
"QTabWidget::pane {\n"
"    top: 1px;\n"
"    border-top: 3px solid rgb(0, 0, 0);\n"
"border-left: 3px solid rgb(0, 0, 0);\n"
"border-right: 3px solid rgb(0, 0, 0);\n"
"border-bottom: 3px solid rgb(0, 0, 0);\n"
"} \n"
"\n"
"QTabBar::tab {\n"
"    color: grey;\n"
"    padding: 10 15 10 15;\n"
"    font: 700 10pt \"Consolas\";\n"
"      background: rgb(31,31,31);\n"
"    /*border-top-right-radius: 1px;\n"
"    border-top-left-radius: 1px;*/\n"
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
"left: 5px;\n"
"top: 0px;\n"
"border: 2px solid blue;\n"
"}b ")
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(parent=self.tab)
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox.setStyleSheet("QGroupBox {\n"
"  border-radius: 2px;\n"
"  margin-top: 1.4em;\n"
"  margin-bottom: 0.5;\n"
"  font: 700 12pt \"Consolas\";\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"  background: transparent;\n"
"  color: white;\n"
"  padding-top: -30px;\n"
"   padding-left: -18px;\n"
"  margin: 0 15 15 15;\n"
"}\n"
"QLabel {\n"
"    color: grey;\n"
"    font: 550 11pt \"Consolas\";\n"
"}\n"
"QSpinBox {\n"
"        font: 600 10pt \"Segoe UI\";\n"
"         background-color:  rgb(41,41,41);\n"
"        color: grey;\n"
"        border-radius: 2px;\n"
"}\n"
"QComboBox {\n"
"        font: 700 10pt \"Segoe UI\";\n"
"         background-color:  rgb(41,41,41);\n"
"        color: grey;\n"
"        border-radius: 2px;\n"
"}")
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_5 = QtWidgets.QWidget(parent=self.groupBox)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_9.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(parent=self.widget_5)
        self.label_7.setMinimumSize(QtCore.QSize(100, 0))
        self.label_7.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.comboBox_4 = QtWidgets.QComboBox(parent=self.widget_5)
        self.comboBox_4.setMinimumSize(QtCore.QSize(0, 35))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.setItemText(0, "")
        self.comboBox_4.addItem("")
        self.horizontalLayout_9.addWidget(self.comboBox_4)
        self.verticalLayout_3.addWidget(self.widget_5)
        self.widget_2 = QtWidgets.QWidget(parent=self.groupBox)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.widget_2)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(parent=self.widget_2)
        self.spinBox.setMinimumSize(QtCore.QSize(100, 35))
        self.spinBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.spinBox.setMaximum(9999)
        self.spinBox.setProperty("value", 300)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_3.addWidget(self.spinBox)
        self.comboBox = QtWidgets.QComboBox(parent=self.widget_2)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 35))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 35))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.verticalLayout_3.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(parent=self.groupBox)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.spinBox_2 = QtWidgets.QSpinBox(parent=self.widget_3)
        self.spinBox_2.setMinimumSize(QtCore.QSize(100, 35))
        self.spinBox_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.spinBox_2.setMaximum(9999)
        self.spinBox_2.setProperty("value", 300)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_4.addWidget(self.spinBox_2)
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.widget_3)
        self.comboBox_2.setMinimumSize(QtCore.QSize(0, 35))
        self.comboBox_2.setMaximumSize(QtCore.QSize(16777215, 35))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_2)
        self.verticalLayout_3.addWidget(self.widget_3)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_5.addItem(spacerItem2, 2, 0, 1, 1)
        self.widget_7 = QtWidgets.QWidget(parent=self.tab_2)
        self.widget_7.setObjectName("widget_7")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_7)
        self.gridLayout_4.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_5.addWidget(self.widget_7, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.tab_2)
        self.groupBox_2.setStyleSheet("QGroupBox {\n"
"  border-radius: 2px;\n"
"  margin-top: 1.4em;\n"
"  margin-bottom: 0.5;\n"
"  font: 700 12pt \"Consolas\";\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"  background: transparent;\n"
"  color: white;\n"
"  padding-top: -30px;\n"
"   padding-left: -18px;\n"
"  margin: 0 15 15 15;\n"
"}\n"
"QLabel {\n"
"    color: grey;\n"
"    font: 550 11pt \"Consolas\";\n"
"}\n"
"QSpinBox {\n"
"        font: 600 10pt \"Segoe UI\";\n"
"         background-color:  rgb(41,41,41);\n"
"        color: grey;\n"
"        border-radius: 2px;\n"
"}\n"
"QComboBox {\n"
"        font: 700 10pt \"Segoe UI\";\n"
"         background-color:  rgb(41,41,41);\n"
"        color: grey;\n"
"        border-radius: 2px;\n"
"}")
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_8 = QtWidgets.QWidget(parent=self.groupBox_2)
        self.widget_8.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_10.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(parent=self.widget_8)
        self.label_8.setMinimumSize(QtCore.QSize(120, 0))
        self.label_8.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.comboBox_5 = QtWidgets.QComboBox(parent=self.widget_8)
        self.comboBox_5.setMinimumSize(QtCore.QSize(0, 35))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.setItemText(0, "")
        self.comboBox_5.addItem("")
        self.horizontalLayout_10.addWidget(self.comboBox_5)
        self.verticalLayout_4.addWidget(self.widget_8)
        self.widget_9 = QtWidgets.QWidget(parent=self.groupBox_2)
        self.widget_9.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_9.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_9.setStyleSheet("")
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_7.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(parent=self.widget_9)
        self.label_4.setMinimumSize(QtCore.QSize(120, 0))
        self.label_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.spinBox_4 = QtWidgets.QSpinBox(parent=self.widget_9)
        self.spinBox_4.setMinimumSize(QtCore.QSize(100, 35))
        self.spinBox_4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.spinBox_4.setMinimum(400)
        self.spinBox_4.setMaximum(720)
        self.spinBox_4.setProperty("value", 400)
        self.spinBox_4.setObjectName("spinBox_4")
        self.horizontalLayout_7.addWidget(self.spinBox_4)
        self.comboBox_6 = QtWidgets.QComboBox(parent=self.widget_9)
        self.comboBox_6.setMinimumSize(QtCore.QSize(0, 35))
        self.comboBox_6.setMaximumSize(QtCore.QSize(16777215, 35))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox_6)
        self.verticalLayout_4.addWidget(self.widget_9)
        self.widget_10 = QtWidgets.QWidget(parent=self.groupBox_2)
        self.widget_10.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_10.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_8.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(parent=self.widget_10)
        self.label_5.setMinimumSize(QtCore.QSize(120, 0))
        self.label_5.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.spinBox_5 = QtWidgets.QSpinBox(parent=self.widget_10)
        self.spinBox_5.setMinimumSize(QtCore.QSize(100, 35))
        self.spinBox_5.setMaximumSize(QtCore.QSize(200, 16777215))
        self.spinBox_5.setMinimum(401)
        self.spinBox_5.setMaximum(720)
        self.spinBox_5.setProperty("value", 720)
        self.spinBox_5.setObjectName("spinBox_5")
        self.horizontalLayout_8.addWidget(self.spinBox_5)
        self.comboBox_7 = QtWidgets.QComboBox(parent=self.widget_10)
        self.comboBox_7.setMinimumSize(QtCore.QSize(0, 35))
        self.comboBox_7.setMaximumSize(QtCore.QSize(16777215, 35))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox_7)
        self.verticalLayout_4.addWidget(self.widget_10)
        self.widget_11 = QtWidgets.QWidget(parent=self.groupBox_2)
        self.widget_11.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_11.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_11.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_6 = QtWidgets.QLabel(parent=self.widget_11)
        self.label_6.setMinimumSize(QtCore.QSize(120, 0))
        self.label_6.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_11.addWidget(self.label_6)
        self.spinBox_6 = QtWidgets.QSpinBox(parent=self.widget_11)
        self.spinBox_6.setMinimumSize(QtCore.QSize(100, 35))
        self.spinBox_6.setMaximumSize(QtCore.QSize(200, 16777215))
        self.spinBox_6.setMaximum(9999)
        self.spinBox_6.setProperty("value", 300)
        self.spinBox_6.setObjectName("spinBox_6")
        self.horizontalLayout_11.addWidget(self.spinBox_6)
        self.comboBox_8 = QtWidgets.QComboBox(parent=self.widget_11)
        self.comboBox_8.setMinimumSize(QtCore.QSize(0, 35))
        self.comboBox_8.setMaximumSize(QtCore.QSize(16777215, 35))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.horizontalLayout_11.addWidget(self.comboBox_8)
        self.verticalLayout_4.addWidget(self.widget_11)
        self.gridLayout_5.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.widget_6 = QtWidgets.QWidget(parent=self.page_widget)
        self.widget_6.setStyleSheet("QPushButton {\n"
"        border: 0px;\n"
"        font: 12pt;\n"
"          background-color: rgb(45, 45, 45);\n"
"        color: grey;\n"
"        padding: 1 1 1 1;\n"
"        font: 700 11pt \"Consolas\";\n"
"border-radius: 2px;\n"
"        }\n"
"QPushButton:hover {\n"
"            background: rgb(55, 55, 55);\n"
"        }\n"
"QPushButton:checked  {\n"
"        border: 0px;\n"
"        background-color : rgb(0, 150, 255);;\n"
"}\n"
"QToolTip{ \n"
"        font: 12pt;\n"
"        color: rgb(100, 100, 100);\n"
"}")
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.CreateWidgetPushButton = QtWidgets.QPushButton(parent=self.widget_6)
        self.CreateWidgetPushButton.setMinimumSize(QtCore.QSize(100, 35))
        self.CreateWidgetPushButton.setMaximumSize(QtCore.QSize(100, 35))
        self.CreateWidgetPushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.CreateWidgetPushButton.setStyleSheet("QPushButton {\n"
"    background: rgb(0, 150, 255);\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgb(51, 180, 255);\n"
"}")
        self.CreateWidgetPushButton.setObjectName("CreateWidgetPushButton")
        self.horizontalLayout_6.addWidget(self.CreateWidgetPushButton)
        self.CancelCreateWidget = QtWidgets.QPushButton(parent=self.widget_6)
        self.CancelCreateWidget.setMinimumSize(QtCore.QSize(100, 35))
        self.CancelCreateWidget.setMaximumSize(QtCore.QSize(100, 35))
        self.CancelCreateWidget.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.CancelCreateWidget.setStyleSheet("QPushButton {\n"
"            font: 650 11pt \"Consolas\";\n"
"}")
        self.CancelCreateWidget.setObjectName("CancelCreateWidget")
        self.horizontalLayout_6.addWidget(self.CancelCreateWidget)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.horizontalLayout_2.addWidget(self.page_widget)
        self.horizontalLayout.addWidget(self.page_selector_widget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        self.CreateWidgetPushButton.clicked.connect(Dialog.onCreateWidget) # type: ignore
        self.CancelCreateWidget.clicked.connect(Dialog.onCancel) # type: ignore
        self.custom_widget_button.clicked.connect(Dialog.onCustomWidgetClicked) # type: ignore
        self.custom_widget_button_2.clicked.connect(Dialog.onCustomWidget2Clicked) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.custom_widget_button.setText(_translate("Dialog", "Custom Widget 1"))
        self.custom_widget_button_2.setText(_translate("Dialog", "Cutom Widget 2"))
        self.groupBox.setTitle(_translate("Dialog", "Widget Size"))
        self.label_7.setText(_translate("Dialog", "Predifined"))
        self.comboBox_4.setItemText(1, _translate("Dialog", "128x128 (128ppi)"))
        self.label.setText(_translate("Dialog", "Width"))
        self.comboBox.setItemText(0, _translate("Dialog", "Pixels (px)"))
        self.comboBox.setItemText(1, _translate("Dialog", "Points (pt)"))
        self.label_2.setText(_translate("Dialog", "Height"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Pixels (px)"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Points (pt)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Dimensions"))
        self.groupBox_2.setTitle(_translate("Dialog", "Widget Properties"))
        self.label_8.setText(_translate("Dialog", "Name"))
        self.comboBox_5.setItemText(1, _translate("Dialog", "400 to 700 (nm)"))
        self.label_4.setText(_translate("Dialog", "Min Wavelength "))
        self.comboBox_6.setItemText(0, _translate("Dialog", "Nanometres (nm)"))
        self.label_5.setText(_translate("Dialog", "Max Wavelength"))
        self.comboBox_7.setItemText(0, _translate("Dialog", "Nanometres (nm)"))
        self.label_6.setText(_translate("Dialog", "Resolution"))
        self.comboBox_8.setItemText(0, _translate("Dialog", "Pixels (px) per Inch"))
        self.comboBox_8.setItemText(1, _translate("Dialog", "Pixels (px) per Centimeter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Content"))
        self.CreateWidgetPushButton.setText(_translate("Dialog", "Create"))
        self.CancelCreateWidget.setText(_translate("Dialog", "Cancel"))
