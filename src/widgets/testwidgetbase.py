from PyQt6.QtWidgets import QWidget
from src.objects.workspace_1 import Ui_Form



#Test CustomWidget
class CustomWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        #Setup UI
        self.ui = Ui_Form()
        self.ui.setupUi(self)
