from PyQt6.QtWidgets import QDialog
from functools import partial
from src.objects.widget_creater_dialog_1 import Ui_Dialog

class WidgetCreatorDialog(QDialog):
    def __init__(self):
        super().__init__()
        
        #Setup UI
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        #Calling Methods
        self.group_buttons_to_pages()




    def group_buttons_to_pages(self):
        for i, button in enumerate(self.ui.widgetTypeButtonGroup.buttons()):
            self.ui.widgetTypeButtonGroup.setId(button,i)

    def WidgetTypePageHandler(self, pageId : int):
        self.ui.stackedWidget.setCurrentIndex(pageId)

    def popUp(self):
        self.exec()

    def closePopUp(self):
        self.close()