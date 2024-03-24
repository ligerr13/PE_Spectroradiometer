from PyQt6.QtCore import QObject
from src.dialogs.measureDialog import MeasureDialog

class NavBar(QObject):
    def __init__(self, resource):
        super().__init__()

        # Setup UI
        self.ui = resource

        #QDialogs
        self.measureDialog = MeasureDialog()

        #Calling Methods
        self.group_buttons_to_pages()


    def group_buttons_to_pages(self):
        for i, button in enumerate(self.ui.NavBarbuttonGroup.buttons()):
            print(self.ui.NavBarbuttonGroup.buttons())
            self.ui.NavBarbuttonGroup.setId(button,i)
