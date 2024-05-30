# Form implementation generated from reading ui file '.\src\ui\workspace_landing_page.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from importlib.resources import path
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(984, 753)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        Form.setStyleSheet("QWidget {background-color: rgb(20, 20, 20);}\n"
"QLineEdit {\n"
"border: 1px solid: grey;\n"
"border-radius: 3px;\n"
"selection-color: yellow;\n"
"selection-background-color: blue;\n"
"}\n"
"QPushButton {\n"
"font: 570 10pt \"Consolas\";\n"
"color:     rgb(190, 190, 190);\n"
"padding: 5 5 5 5;\n"
"margin: 0 0 -1 0;\n"
"}\n"
"QPushButton:hover {\n"
"            color: white;\n"
"        }\n"
"QPushButton:checked  {\n"
"        border: 0px;\n"
"        border-radius: 0px;\n"
"        border-bottom: 5px solid  rgb(63, 101, 255);\n"
"        color: white;\n"
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
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_2 = QtWidgets.QWidget(parent=self.widget)
        self.widget_2.setMaximumSize(QtCore.QSize(200, 200))
        self.widget_2.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.widget_2.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.closeButton = QtWidgets.QPushButton(parent=self.widget_2)
        self.closeButton.setObjectName("closeButton")
        self.gridLayout_2.addWidget(self.closeButton, 1, 1, 1, 1)
        self.createWSButton = QtWidgets.QPushButton(parent=self.widget_2)
        self.createWSButton.setMaximumSize(QtCore.QSize(70, 30))
        self.createWSButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.createWSButton.setStyleSheet("")
        self.createWSButton.setObjectName("createWSButton")
        self.gridLayout_2.addWidget(self.createWSButton, 1, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget_2)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.lineEdit.setStyleSheet("QLabel {\n"
"    font: 700 11pt \"Consolas\";\n"
"    color: white;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.gridLayout_3.addWidget(self.widget_2, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.actioncreate_on_enter = QtGui.QAction(parent=Form)
        self.actioncreate_on_enter.setObjectName("actioncreate_on_enter")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.closeButton.setText(_translate("Form", "Close"))
        self.createWSButton.setText(_translate("Form", "Create"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Type the name of your Workspace"))
        self.actioncreate_on_enter.setText(_translate("Form", "create_on_enter"))
        self.actioncreate_on_enter.setShortcut(_translate("Form", "Return"))

