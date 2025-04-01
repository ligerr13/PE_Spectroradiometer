import sys
import json
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QRect

class SerializableWidget(QWidget):
    def __init__(self, widget_id, widget_type, data=None):
        super().__init__()
        self.widget_id = widget_id
        self.widget_type = widget_type
        self.sub_type = ""
        self.objectName = None
        self.data = data or {}

    def get_widget_data(self):
        geometry = self.geometry()
        return {
            'id': self.widget_id,
            'type': self.widget_type,
            'sub-type': self.sub_type,
            'uniqe_name': self.objectName,
            'geometry': {
                'x': geometry.x(),
                'y': geometry.y(),
                'width': geometry.width(),
                'height': geometry.height()
            },
            'data': self.data
        }

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