# Form implementation generated from reading ui file '.\src\ui\measure_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(477, 531)
        Dialog.setStyleSheet("background-color: rgb(20, 20, 20); \n"
"border-radius: 5px;\n"
"border: 0px;")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(parent=self.widget)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_2.setMinimumSize(QtCore.QSize(0, 35))
        self.label_2.setStyleSheet("font: 623 14pt \"Segoe UI\";\n"
"color: rgb(233, 233, 233);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_7 = QtWidgets.QWidget(parent=self.widget)
        self.widget_7.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_7.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_7.setStyleSheet("QWidget {\n"
"    background-color: rgb(31, 31, 31);\n"
"    color:white;\n"
"    border-radius: 0px;\n"
"    background-color: rgb(35, 35, 35);\n"
"}\n"
"Line {\n"
"    background-color: rgba(129, 129, 129, 50);\n"
"}\n"
"QPushButton {\n"
"        font: 700 10pt \"Segoe UI\";\n"
"}")
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_5.setMaximumSize(QtCore.QSize(150, 50))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_5.setStyleSheet("QPushButton:hover {\n"
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
        self.pushButton_5.setCheckable(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_4.addWidget(self.pushButton_5)
        self.line = QtWidgets.QFrame(parent=self.widget_7)
        self.line.setMinimumSize(QtCore.QSize(1, 0))
        self.line.setMaximumSize(QtCore.QSize(1, 16777215))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_4.addWidget(self.line)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_6.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_6.setStyleSheet("QPushButton:hover {\n"
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
        self.pushButton_6.setCheckable(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_4.addWidget(self.pushButton_6)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        self.pushButton_6.clicked.connect(Dialog.onAccept) # type: ignore
        self.pushButton_5.clicked.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.widget.setStyleSheet(_translate("Dialog", "0"))
        self.label_2.setText(_translate("Dialog", "New Measurement"))
        self.pushButton_5.setText(_translate("Dialog", "Cancel"))
        self.pushButton_6.setText(_translate("Dialog", "Start"))
