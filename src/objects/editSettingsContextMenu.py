# Form implementation generated from reading ui file '.\src\ui\editSettingsContextMenu.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 341)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        Form.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.ActionsContextMenu)
        Form.setAcceptDrops(False)
        Form.setStyleSheet("QMenu {\n"
"    font: 10pt \"Consolas\";\n"
"    background-color: rgb(51, 51, 51);\n"
"    border: 1px solid  grey;\n"
"    border-radius: 3px;\n"
"    color:rgb(190, 190, 190);\n"
"    padding: 3 3 3 3;\n"
"    icon-size: 20px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    spacing: 1px;\n"
"    padding: 5 20 5 20;\n"
"    background: transparent;\n"
"}\n"
"QMenu:item:selected {\n"
"    background-color:  rgb(63, 101, 255);\n"
"    border-radius: 3px;\n"
"    color: rgb(230,230,230)\n"
"}")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.actionShow_Workspace_Grid = QtGui.QAction(parent=Form)
        self.actionShow_Workspace_Grid.setCheckable(True)
        self.actionShow_Workspace_Grid.setChecked(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\src\\ui\\../../resources/icons/toggle-button-off.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap(".\\src\\ui\\../../resources/icons/toggle-button-on.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.actionShow_Workspace_Grid.setIcon(icon)
        self.actionShow_Workspace_Grid.setObjectName("actionShow_Workspace_Grid")
        self.actionChange_Theme = QtGui.QAction(parent=Form)
        self.actionChange_Theme.setObjectName("actionChange_Theme")
        self.actionLight = QtGui.QAction(parent=Form)
        self.actionLight.setObjectName("actionLight")
        self.actionDark = QtGui.QAction(parent=Form)
        self.actionDark.setObjectName("actionDark")
        self.actionUndo = QtGui.QAction(parent=Form)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtGui.QAction(parent=Form)
        self.actionRedo.setObjectName("actionRedo")
        self.actionPaste = QtGui.QAction(parent=Form)
        self.actionPaste.setObjectName("actionPaste")
        self.actionCopy = QtGui.QAction(parent=Form)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCut = QtGui.QAction(parent=Form)
        self.actionCut.setObjectName("actionCut")
        self.actionSelect_All = QtGui.QAction(parent=Form)
        self.actionSelect_All.setObjectName("actionSelect_All")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.actionShow_Workspace_Grid.setText(_translate("Form", "Show Workspace Grid"))
        self.actionChange_Theme.setText(_translate("Form", "Change Theme"))
        self.actionChange_Theme.setToolTip(_translate("Form", "Change Theme"))
        self.actionLight.setText(_translate("Form", "Light"))
        self.actionDark.setText(_translate("Form", "Dark"))
        self.actionUndo.setText(_translate("Form", "Undo"))
        self.actionUndo.setShortcut(_translate("Form", "Ctrl+Z"))
        self.actionRedo.setText(_translate("Form", "Redo"))
        self.actionRedo.setShortcut(_translate("Form", "Ctrl+Shift+Z"))
        self.actionPaste.setText(_translate("Form", "Paste"))
        self.actionPaste.setShortcut(_translate("Form", "Ctrl+V"))
        self.actionCopy.setText(_translate("Form", "Copy"))
        self.actionCopy.setShortcut(_translate("Form", "Ctrl+C"))
        self.actionCut.setText(_translate("Form", "Cut"))
        self.actionCut.setShortcut(_translate("Form", "Ctrl+X"))
        self.actionSelect_All.setText(_translate("Form", "Select All"))
        self.actionSelect_All.setShortcut(_translate("Form", "Ctrl+A"))
