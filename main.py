from PyQt6.QtWidgets import QApplication, QMainWindow
from src.main_window import Ui_MainWindow
import qdarktheme
from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.prev_button = None

        self.ui.pushButton.clicked.connect(self.handle_navbar_button_backgorund_signal)
        self.ui.pushButton_2.clicked.connect(self.handle_navbar_button_backgorund_signal)
        self.ui.pushButton_3.clicked.connect(self.handle_navbar_button_backgorund_signal)

    def handle_navbar_button_backgorund_signal(self):
            button = self.sender()
            
            button.setStyleSheet("background-color: #33ccff")
            
            if self.prev_button is not None:
                self.prev_button.setStyleSheet("background-color: transparent, border: 0px")
            
            self.prev_button = button

if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(qdarktheme.load_stylesheet("light"))

    window = MyApp()
    window.show()
    app.exec()
