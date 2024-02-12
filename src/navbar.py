from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QPushButton

from src.resource_1 import Ui_MainWindow



class NavBar(QObject):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.ui = Ui_MainWindow()
        self.ui.setupUi(parent)

        self.prev_button = None

        #Signals and Connections
        self.ui.pushButton.clicked.connect(lambda: self.handle_navbar_button_background_signal(self.ui.pushButton))
        self.ui.pushButton_2.clicked.connect(lambda: self.handle_navbar_button_background_signal(self.ui.pushButton_2))
        self.ui.pushButton_3.clicked.connect(lambda: self.handle_navbar_button_background_signal(self.ui.pushButton_3))

    def handle_navbar_button_background_signal(self, button):
        if button == self.prev_button:
            self.prev_button.setStyleSheet("border: 0px")
            self.prev_button = None
        else:
            if self.prev_button is not None:
                self.prev_button.setStyleSheet("border: 0px")
            
            button.setStyleSheet("background-color: #3366cc; border: 2px solid white")
            self.prev_button = button
