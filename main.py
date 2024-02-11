from PyQt6.QtWidgets import QApplication, QMainWindow
from src.main_window import Ui_MainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication([])
    window = MyApp()
    window.show()
    app.exec()
