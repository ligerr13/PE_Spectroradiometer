import os
import json
from src.instrument.config.enums import DataBlockNumber, DataFormat, DataMode, ModeSelect, SpectralRange

class JsonBuilder:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.result_data = {}

    def Merge(self, dict_1, dict_2):
        result = dict_1 | dict_2
        return result
    
    def build(self):
        json_structure = {self.__class__.__name__: self.result_data}
        data_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'instrument/data'))
        filename = f"{self.file_name}.json"
        file_path = os.path.join(data_folder, filename)

        if os.path.exists(file_path):
            with open(file_path, 'r') as existing_file:
                existing_data = json.load(existing_file)
                json_structudict_3 = self.Merge(existing_data, json_structure)

                with open(file_path, 'w') as jsonfile:
                    json.dump(json_structudict_3, jsonfile, indent=4)
    
        else:
            with open(file_path, 'w') as jsonfile:
                json.dump(json_structure, jsonfile, indent=4, )


class ColorimetricJsonBuilder(JsonBuilder):
    def __init__(self, file_name: str, data):
        super().__init__(file_name)

        # print("NOTRAW:",data)

        self.colorimetric_keys = [
            "Le", "Lv", "X", "Y", "Z", "x", "y", "u'", "v'", "T", "delta uv", "lambda d", "Pe",
            "X10", "Y10", "Z10", "x10", "y10", "u'10", "v'10", "T10", "delta uv10", "lambda d10", "Pe10",
        ]

        x = data.split(",")
        self.result_data = {"Colorimetric Data": {}}
        for key, value in zip(self.colorimetric_keys, x):
            self.result_data["Colorimetric Data"][key] = {"value": value, "switch": 0}

class MeasurementJsonBuilder(JsonBuilder):
    def __init__(self, file_name: str, data):
        super().__init__(file_name)

        self.meascon_keys = [
            "Speed mode", "Sync mode", "Integration time", "Internal ND filter",
            "Optional close-up lens", "Optional external ND filter", "Measurement angle", "Calibration channel"
        ]
        x = data.split(",")
        self.result_data = {"Measurement Conditions": {}}
        for key, value in zip(self.meascon_keys, x):
            self.result_data["Measurement Conditions"][key] = {"value": value, "switch": 0}

class SpectralJsonBuilder(JsonBuilder):
    def __init__(self, file_name: str,  data):
        super().__init__(file_name)
        self.result_data = {"Spectral data": {data}}
        self.result_data["Spectral data"] = {"value": data, "switch": 0}


class JsonBuilderFactory:
    @staticmethod
    def create_builder(builder_type, file_name, *args, **kwargs):
        if builder_type == DataMode.COLORIMETRIC_DATA:
            return ColorimetricJsonBuilder(file_name, *args, **kwargs)
        elif builder_type == DataMode.MEASUREMENT_CONDITIONS:
            return MeasurementJsonBuilder(file_name, *args, **kwargs)
        elif builder_type == DataMode.SPECTRAL_DATA:
            return SpectralJsonBuilder(file_name, *args, **kwargs)
        else:
            print("Invalid builder type")