from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableView
from PyQt6.QtGui import QStandardItemModel, QStandardItem



class DataViewTestWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Data View példa")
        self.setGeometry(100, 100, 600, 400)

        self.setupDataView()

    def setupDataView(self):
        # Modell létrehozása
        model = QStandardItemModel(4, 3) # 4 sor, 3 oszlop

        # Adatok hozzáadása a modellhez
        for row in range(4):
            for column in range(3):
                item = QStandardItem("Sor {} Oszlop {}".format(row, column))
                model.setItem(row, column, item)

        # Data view létrehozása és modell beállítása
        data_view = QTableView()
        data_view.setModel(model)

        layout = QVBoxLayout(self) # QVBoxLayout a QWidget-en belül
        layout.addWidget(data_view) # QTableView hozzáadása a QVBoxLayout-hoz
        layout.setContentsMargins(0, 0, 0, 0) # Marginok beállítása nullára
        layout.setSpacing(0) # Térköz beállítása nullára