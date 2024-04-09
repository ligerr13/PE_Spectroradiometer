from PyQt6.QtCore import QObject, Qt, QAbstractTableModel, QVariant, QModelIndex, QTimer
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QDialog, QProgressBar, QHeaderView, QStyleOptionProgressBar
from src.dialogs.connectionConfigDialog import ConnectionConfigDialog
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QStyle, QStyledItemDelegate, QStyleOptionProgressBar,QApplication, QTableView
from PyQt6.QtGui import QStandardItem, QStandardItemModel
from PyQt6.QtCore import Qt

data = [("1", "meres1", 10, "2022-04-09"), ("2", "meres2", 23, "2023-04-09"),
        ("3", "meres_lajosnak", 30, "2024-04-09"), ("4", "meres_pistanak_nagyon", 55, "2022-04-03"), 
        ("5", "meres3", 100, "2022-04-01")]

class ProgressDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        progress = index.data(Qt.ItemDataRole.UserRole + 1000)

        opt = QStyleOptionProgressBar()
        opt.rect = option.rect
        opt.palette = option.palette
        opt.fontMetrics = option.fontMetrics
        opt.minimum = 0
        opt.maximum = 100
        opt.progress = progress
        opt.text = f"{progress}%"
        opt.textVisible = True
        opt.state |= QStyle.StateFlag.State_Horizontal

        style = QApplication.style()
        style.drawControl(QStyle.ControlElement.CE_ProgressBar, opt, painter, option.widget)


class Footer(QObject):
    def __init__(self, resource):
        # Setup UI
        self.ui = resource
        self.connection_toolbutton = self.ui.toolButton_2
        self.progressTableView = self.ui.progressTableView

        #QDialogs
        self.connectionConfigDialog = ConnectionConfigDialog()
        
        delegate = ProgressDelegate(self.progressTableView)
        self.progressTableView.setItemDelegateForColumn(3, delegate)

        model = QStandardItemModel(0, 3)
        model.setHorizontalHeaderLabels(["ID", "Measurement","Date", "Progress"])


        for _id, _name, _progress, _date in data:
            it_id = QStandardItem(_id)
            it_name = QStandardItem(_name)
            it_date = QStandardItem(_date)
            it_progress = QStandardItem()
            it_progress.setData(_progress, Qt.ItemDataRole.UserRole + 1000)
            model.appendRow([it_id, it_name,it_date, it_progress])
        
        self.progressTableView.setModel(model)