from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QPushButton
from functools import partial

class NavBar(QObject):
    def __init__(self, resource):
        super().__init__()
        self.ui = resource
        self.prev_button = None

        #Calling Methods
        self.group_butttons_to_pages()
        self.HandleButtonVisuals()




    def group_butttons_to_pages(self):
        for i, button in enumerate(self.ui.NavBarbuttonGroup.buttons()):
            self.ui.NavBarbuttonGroup.setId(button,i)

    def HandleButtonVisuals(self):
        for i, button in enumerate(self.ui.NavBarbuttonGroup.buttons()):
            button.clicked.connect(partial(self.handle_navbar_button_background_signal, button))
            
    def handle_navbar_button_background_signal(self, button):
        if button == self.prev_button:
            self.prev_button.setStyleSheet("QPushButton {border: 0px;}QPushButton:hover {background: rgb(55, 55, 55);}")
            self.prev_button = None
        else:
            if self.prev_button is not None:
                self.prev_button.setStyleSheet("QPushButton {border: 0px;}QPushButton:hover {background: rgb(55, 55, 55);}")
            
            button.setStyleSheet("QPushButton {border: 0px;background-color: rgb(63, 101, 255);}, QPushButton:hover {background: rgb(55, 55, 55);}")
            self.prev_button = button
