from PyQt6.QtCore import QObject


class NodeBoard(QObject):
    def __init__(self, resource):
        super().__init__()
        self.ui = resource

        self.prev_button = None

        #Signals and Connections
        self.ui.pushButton_4.clicked.connect(lambda: self.handle_navbar_button_background_signal(self.ui.pushButton_4))

        self.ui.pushButton_5.clicked.connect(lambda: self.handle_navbar_button_background_signal(self.ui.pushButton_5))

        self.ui.pushButton_6.clicked.connect(lambda: self.handle_navbar_button_background_signal(self.ui.pushButton_6))


    def handle_navbar_button_background_signal(self, button):
        if button == self.prev_button:
            self.prev_button.setStyleSheet("border: 0px")
            self.prev_button = None
        else:
            if self.prev_button is not None:
                self.prev_button.setStyleSheet("border: 0px")
            
            button.setStyleSheet("background-color: rgba(0, 0, 0, 50); border: 0px")
            self.prev_button = button
