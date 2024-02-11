from PyQt6.QtWidgets import QApplication, QMainWindow
from src.main_window import Ui_MainWindow
import qdarktheme

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
            print(self, " Signal Test")

if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(qdarktheme.load_stylesheet("light"))

    window = MyApp()
    window.show()
    app.exec()
