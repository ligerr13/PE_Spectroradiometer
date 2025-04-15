import sys
import json
from abc import ABCMeta, abstractmethod
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QRect

class MetaQWidget(type(QWidget), ABCMeta):
    pass

class SerializableWidget(QWidget, metaclass=MetaQWidget):
    def __init__(self, widget_id, widget_type, data=None):
        super().__init__()
        self.widget_id = widget_id
        self.widget_type = widget_type
        self.sub_type = ""
        self.objectName = None
        self.data = data or {}

    @abstractmethod
    def get_widget_data(self):
        pass

    def set_widget_data(self, widget_data):
        self.widget_id = widget_data['id']
        self.widget_type = widget_data['type']
        self.sub_type = widget_data['sub-type']
        self.data = widget_data['data']
        self.setGeometry(QRect(
            widget_data['geometry']['x'],
            widget_data['geometry']['y'],
            widget_data['geometry']['width'],
            widget_data['geometry']['height']
        ))