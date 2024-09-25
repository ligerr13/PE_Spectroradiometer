from PyQt6.QtWidgets import QDialog
from src.objects.widget_creater_dialog import Ui_Dialog

class WidgetCreatorDialog(QDialog):
    def __init__(self):
        super().__init__()
        
        #Setup UI
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        #Calling Methods

    def onCustomWidgetClicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def onCustomWidget2Clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        
    def onCreateWidget(self):
        print("Creating Widget")
        self.accept()

    def onCancel(self):
        self.reject()

    def popUp(self):
        self.exec()

    def closePopUp(self):
        self.close()