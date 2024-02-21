from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QPushButton
from functools import partial

class NavBar(QObject):
    def __init__(self, resource):
        super().__init__()
        self.ui = resource
        self.prev_button = None

        #Calling Methods
        self.group_buttons_to_pages()
        self.HandleButtonVisuals()


    def group_buttons_to_pages(self):
        for i, button in enumerate(self.ui.NavBarbuttonGroup.buttons()):
            self.ui.NavBarbuttonGroup.setId(button,i)

    def HandleButtonVisuals(self):
        for i, button in enumerate(self.ui.NavBarbuttonGroup.buttons()):
            button.clicked.connect(partial(self.handle_navbar_button_background_signal, button))
        
    #change to toggle like in nodeboard
    def handle_navbar_button_background_signal(self, button):
        if button == self.prev_button:
            self.prev_button = None
        else:
            self.prev_button = button
