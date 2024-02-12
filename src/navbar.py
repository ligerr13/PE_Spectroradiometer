from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QPushButton


class NavBar(QObject):
    def __init__(self, resource):
        super().__init__()
        self.ui = resource

        self.prev_button = None

        #Signals and Connections
        self.ui.pushButton.clicked.connect(lambda: self.handle_navbar_button_background_signal(self.ui.pushButton))
        self.ui.pushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))

        self.ui.pushButton_2.clicked.connect(lambda: self.handle_navbar_button_background_signal(self.ui.pushButton_2))
        self.ui.pushButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))

        self.ui.pushButton_3.clicked.connect(lambda: self.handle_navbar_button_background_signal(self.ui.pushButton_3))
        self.ui.pushButton_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))


    def handle_navbar_button_background_signal(self, button):
        if button == self.prev_button:
            self.prev_button.setStyleSheet("border: 0px")
            self.prev_button = None
        else:
            if self.prev_button is not None:
                self.prev_button.setStyleSheet("border: 0px")
            
            button.setStyleSheet("background-color: rgba(0, 0, 0, 50); border: 0px")
            self.prev_button = button
