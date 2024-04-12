from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableView
from PyQt6.QtGui import QStandardItemModel, QStandardItem
# import pandas as pd
import json


class JSONreader:
    def __init__(self, filename):
        self.filename = filename
    def read(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"The File '{self.filename}' does not exist.")
            return None
        except json.JSONDecodeError:
            print(f"Not supported JSON format.")
            return None


class DataViewTestWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Data View példa")
        self.setGeometry(100, 100, 600, 400)

        self.setupDataView()

    def setupDataView(self):
        model = QStandardItemModel(4, 3)

        for row in range(4):
            for column in range(3):
                item = QStandardItem("Sor {} Oszlop {}".format(row, column))
                model.setItem(row, column, item)

        data_view = QTableView()
        data_view.setModel(model)

        layout = QVBoxLayout(self)
        layout.addWidget(data_view)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)