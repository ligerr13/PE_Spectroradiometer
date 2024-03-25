# Form implementation generated from reading ui file '.\ui\widget_creater_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(506, 541)
        Dialog.setStyleSheet("background-color: rgb(20, 20, 20); \n"
"border-radius: 5px;")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(parent=self.widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_6 = QtWidgets.QWidget(parent=self.widget)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_6.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_6.setStyleSheet("color:white;\n"
"border-radius: 5px;\n"
"background-color: rgb(35, 35, 35);")
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget_6)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
"        border: 0px;\n"
"        font: 700 10pt \"Segoe UI\";\n"
"        color: rgb(43, 81, 235);\n"
"        background-color: rgb(0, 33, 71);\n"
"        }\n"
"QPushButton:hover {\n"
"          background-color: rgb(10, 43, 81);\n"
"        }\n"
"QPushButton:checked  {\n"
"        border: 0px;\n"
"}\n"
"QPushTip{ \n"
"        font: 12pt;\n"
"        color: rgb(100, 100, 100);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget_6)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"        border: 0px;\n"
"        font: 700 10pt \"Segoe UI\";\n"
"        border :1.5px solid rgb(55, 55, 55);\n"
"        }\n"
"QPushButton:hover {\n"
"            background: rgb(55, 55, 55);\n"
"        }\n"
"QPushButton:checked  {\n"
"        border: 0px;\n"
"        background-color: rgb(45, 45, 45);\n"
"}\n"
"QPushTip{ \n"
"        font: 12pt;\n"
"        color: rgb(100, 100, 100);\n"
"}")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.pushButton_2)
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.widget_6)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"        border: 0px;\n"
"        font: 700 10pt \"Segoe UI\";\n"
"         background: rgb(55, 55, 55);\n"
"        border :3px solid rgb(55, 55, 55);\n"
"        }\n"
"QPushButton:hover {\n"
"            background: rgb(43, 81, 235);\n"
"            border :3px solid rgb(63, 101, 255);\n"
"        }\n"
"QPushButton:checked  {\n"
"        border: 0px;\n"
"        background: rgb(43, 81, 235);\n"
"        border :3px solid rgb(63, 101, 255);\n"
"}\n"
"QPushTip{ \n"
"        font: 12pt;\n"
"        color: rgb(100, 100, 100);\n"
"}")
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.buttonGroup_2.addButton(self.pushButton_3)
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.verticalLayout.addWidget(self.widget_6)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        self.pushButton_3.clicked.connect(Dialog.onAccept) # type: ignore
        self.pushButton_2.clicked.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.widget.setStyleSheet(_translate("Dialog", "0"))
        self.pushButton.setText(_translate("Dialog", "Preview"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.pushButton_3.setText(_translate("Dialog", "Create"))
