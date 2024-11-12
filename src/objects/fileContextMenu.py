# Form implementation generated from reading ui file '.\src\ui\fileContextMenu.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(470, 406)
        Form.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        Form.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.ActionsContextMenu)
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
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.actionSaveAs = QtGui.QAction(parent=Form)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionClose_Workspace = QtGui.QAction(parent=Form)
        self.actionClose_Workspace.setObjectName("actionClose_Workspace")
        self.actionClose_Window = QtGui.QAction(parent=Form)
        self.actionClose_Window.setObjectName("actionClose_Window")
        self.actionNew_Workspace = QtGui.QAction(parent=Form)
        self.actionNew_Workspace.setObjectName("actionNew_Workspace")
        self.actionSave_All = QtGui.QAction(parent=Form)
        self.actionSave_All.setObjectName("actionSave_All")
        self.actionHome_Page = QtGui.QAction(parent=Form)
        self.actionHome_Page.setObjectName("actionHome_Page")
        self.actionClose_All_Workspace = QtGui.QAction(parent=Form)
        self.actionClose_All_Workspace.setObjectName("actionClose_All_Workspace")
        self.actionopen_workspace_form_file = QtGui.QAction(parent=Form)
        self.actionopen_workspace_form_file.setObjectName("actionopen_workspace_form_file")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.actionSaveAs.setText(_translate("Form", "Save As"))
        self.actionSaveAs.setShortcut(_translate("Form", "Ctrl+S"))
        self.actionClose_Workspace.setText(_translate("Form", "Close Workspace"))
        self.actionClose_Workspace.setShortcut(_translate("Form", "Ctrl+W"))
        self.actionClose_Window.setText(_translate("Form", "Close Window"))
        self.actionNew_Workspace.setText(_translate("Form", "New Workspace"))
        self.actionNew_Workspace.setShortcut(_translate("Form", "Ctrl+N"))
        self.actionSave_All.setText(_translate("Form", "Save All"))
        self.actionSave_All.setShortcut(_translate("Form", "Ctrl+Shift+S"))
        self.actionHome_Page.setText(_translate("Form", "Home Page"))
        self.actionClose_All_Workspace.setText(_translate("Form", "Close All Workspace"))
        self.actionopen_workspace_form_file.setText(_translate("Form", "Open Workspace From File"))
