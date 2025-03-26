# Form implementation generated from reading ui file 'src/ui/add_text_to_scene_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from importlib.resources import path
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(418, 528)
        Dialog.setStyleSheet("QDialog {background-color: rgb(30, 30, 30);\n"
"}\n"
"\n"
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
"        border-bottom: 3px solid  rgb(63, 101, 255);\n"
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
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_7 = QtWidgets.QWidget(parent=self.widget)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget_7)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/ui/../../resources/icons/align-left.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(True)
        self.pushButton.setObjectName("pushButton")
        self.alignButtonGroup = QtWidgets.QButtonGroup(Dialog)
        self.alignButtonGroup.setObjectName("alignButtonGroup")
        self.alignButtonGroup.addButton(self.pushButton)
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget_7)
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_2.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("src/ui/../../resources/icons/format.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.alignButtonGroup.addButton(self.pushButton_2)
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.widget_7)
        self.pushButton_3.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_3.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("src/ui/../../resources/icons/align-right.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setChecked(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.alignButtonGroup.addButton(self.pushButton_3)
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.widget_3 = QtWidgets.QWidget(parent=self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.widget_3)
        self.pushButton_4.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_4.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("src/ui/../../resources/icons/bold-text.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.widget_3)
        self.pushButton_5.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_5.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("src/ui/../../resources/icons/italic-font.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.widget_3)
        self.pushButton_6.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_6.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_6.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("src/ui/../../resources/icons/underline-text.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget_13 = QtWidgets.QWidget(parent=self.widget)
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget_13)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 45))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_6.addWidget(self.lineEdit)
        self.verticalLayout_2.addWidget(self.widget_13)
        self.widget_5 = QtWidgets.QWidget(parent=self.widget)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(parent=self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.fontComboBox = QtWidgets.QFontComboBox(parent=self.widget_5)
        self.fontComboBox.setObjectName("fontComboBox")
        self.horizontalLayout_4.addWidget(self.fontComboBox)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(parent=self.widget)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(parent=self.widget_6)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.widget_6)
        self.pushButton_10.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_10.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setChecked(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.szieButtonGroup = QtWidgets.QButtonGroup(Dialog)
        self.szieButtonGroup.setObjectName("szieButtonGroup")
        self.szieButtonGroup.addButton(self.pushButton_10)
        self.horizontalLayout_5.addWidget(self.pushButton_10)
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.widget_6)
        self.pushButton_7.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_7.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.szieButtonGroup.addButton(self.pushButton_7)
        self.horizontalLayout_5.addWidget(self.pushButton_7)
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.widget_6)
        self.pushButton_9.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_9.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.szieButtonGroup.addButton(self.pushButton_9)
        self.horizontalLayout_5.addWidget(self.pushButton_9)
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.widget_6)
        self.pushButton_12.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_12.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.szieButtonGroup.addButton(self.pushButton_12)
        self.horizontalLayout_5.addWidget(self.pushButton_12)
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.widget_6)
        self.pushButton_11.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_11.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.szieButtonGroup.addButton(self.pushButton_11)
        self.horizontalLayout_5.addWidget(self.pushButton_11)
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.widget_6)
        self.pushButton_8.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_8.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.szieButtonGroup.addButton(self.pushButton_8)
        self.horizontalLayout_5.addWidget(self.pushButton_8)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(parent=Dialog)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_9 = QtWidgets.QWidget(parent=self.widget_2)
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_10 = QtWidgets.QWidget(parent=self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(parent=self.widget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.verticalLayout_4.addWidget(self.widget_10)
        self.widget_4 = QtWidgets.QWidget(parent=self.widget_9)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_4.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget_9)
        self.widget_8 = QtWidgets.QWidget(parent=self.widget_2)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_11 = QtWidgets.QWidget(parent=self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy)
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_11)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(parent=self.widget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.verticalLayout_3.addWidget(self.widget_11)
        self.widget_12 = QtWidgets.QWidget(parent=self.widget_8)
        self.widget_12.setObjectName("widget_12")
        self.verticalLayout_3.addWidget(self.widget_12)
        self.horizontalLayout.addWidget(self.widget_8)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_14 = QtWidgets.QWidget(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy)
        self.widget_14.setObjectName("widget_14")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_14)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_13 = QtWidgets.QPushButton(parent=self.widget_14)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_7.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(parent=self.widget_14)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_7.addWidget(self.pushButton_14)
        self.verticalLayout.addWidget(self.widget_14)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Font"))
        self.label.setText(_translate("Dialog", "Font "))
        self.label_2.setText(_translate("Dialog", "Size"))
        self.pushButton_10.setText(_translate("Dialog", "12"))
        self.pushButton_7.setText(_translate("Dialog", "14"))
        self.pushButton_9.setText(_translate("Dialog", "16"))
        self.pushButton_12.setText(_translate("Dialog", "18"))
        self.pushButton_11.setText(_translate("Dialog", "22"))
        self.pushButton_8.setText(_translate("Dialog", "30"))
        self.label_3.setText(_translate("Dialog", "Color"))
        self.label_4.setText(_translate("Dialog", "Backgorund"))
        self.pushButton_13.setText(_translate("Dialog", "Cancel"))
        self.pushButton_14.setText(_translate("Dialog", "Save"))

