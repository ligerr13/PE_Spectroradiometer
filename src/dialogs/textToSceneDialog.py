from PyQt6.QtWidgets import QTreeWidget, QTreeWidgetItem, QDialog, QGraphicsDropShadowEffect
from src.objects.add_text_to_scene_dialog import Ui_Dialog
from PyQt6 import QtCore
class TextToSceneDialog(QDialog):
    def __init__(self):
        super().__init__()
        
        #Setup UI
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        # self.setWindowOpacity(0.95)
        shadow = QGraphicsDropShadowEffect()
        self.setGraphicsEffect(shadow)

        #Calling Methods


    def closeEvent(self, event):
        if self.result() == QDialog.DialogCode.Accepted:
            print("Dialog accepted")
        else:
            print("Dialog rejected")
        event.accept()

    def onAccept(self):
        self.accept()

    def popUp(self):
        self.exec()

    def closePopUp(self):
        self.close()