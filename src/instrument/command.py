from abc import ABC, abstractmethod
from .message import Message
from .connection import Connection
from typing import Union
from enum import Enum
import os, json

delimiter = b'\n'

class Command(ABC):
    def __init__(self, *args, **kwargs):
        self.connection = None

        if args:
            self.params = args[0]
        else:
            self.params = kwargs.get('params', {})

    @abstractmethod
    def prepare_message(self) -> Message:

        """
        Prepares the message.

        Returns:
            bytes: The received message.
        """
        pass

    @abstractmethod
    async def send_message(self, msg: Message):

        """
        Sends a message to the instrument.

        Args:
            message (bytes): The message to be sent.
        """
        pass
        
    async def receive_message(self) -> bytes:

        """
        Receives message from the instrument.

        Returns:
            bytes: The received message.
        """
        try:
            return self.connection.readline()
        except Exception as err:
            raise Exception("An error occurred while reading data: ", err)
        
    
    def exec_write(self, message: bytes) -> bytes:
        if not self.connection:
            self.connection = Connection.get_shared_connection()
        
        self.connection.write(message)


class ModeSelect(Enum):
    ENABLED = 1
    DISABLED = 0

class RMTS(Command):
    def __init__(self, switch: ModeSelect):
        super().__init__(params={"switch": switch})

    def prepare_message(self) -> Message:
        message_content = b'RMTS,' + bytes(str(self.params["switch"].value), 'utf-8') + delimiter
        return Message(params=self.params, message=message_content)
    
    async def send_message(self, msg: Message):
        try:
            self.exec_write(msg.message)

            resp1 = await self.receive_message()
            return resp1
        except Exception as err:
            raise Exception("An error occurred while sending data: ", err)

    
class MSWE(Command):
    def __init__(self, switch: ModeSelect):
        super().__init__(params={"switch": switch})

    def prepare_message(self) -> Message:
        message_content = b'MSWE,' + bytes(str(self.params["switch"].value), 'utf-8') + delimiter
        return Message(params=self.params, message=message_content)
    
    async def send_message(self, msg: Message):
        try:
        
            self.exec_write(msg.message)

            resp1 = await self.receive_message()
            return resp1
        except Exception as err:
            print("An error occurred while sending data: ", err)
        

class MEAS(Command):
    def __init__(self, switch: ModeSelect):
        super().__init__(params={"switch": switch})

    def prepare_message(self) -> Message:
        message_content = b'MEAS,' + bytes(str(self.params["switch"].value), 'utf-8') + delimiter
        return Message(params=self.params, message=message_content)
    
    async def send_message(self, msg: Message):
        try:
            self.exec_write(msg.message)
            
            resp1 = await self.receive_message()
            resp2 = await self.receive_message()

            return resp1, resp2
        except Exception as err:
            print("An error occurred while sending data: ", err)


class DataMode(Enum):
    MEASUREMENT_CONDITIONS = 0
    SPECTRAL_DATA = 1
    COLORIMETRIC_DATA = 2

class DataFormat(Enum):
    ALPHANUMERIC = 0
    HEXADECIMAL = 1

class DataBlockNumber(Enum):
    MEASUREMENT_CONDITIONS = 1
    COLORIMETRIC_DATA = 0

class SpectralRange(Enum):
    RANGE_380_TO_479 = 1
    RANGE_480_TO_579 = 2  
    RANGE_580_TO_679 = 3  
    RANGE_680_TO_780 = 4 


class MEDR(Command):
    def __init__(self, data_mode: DataMode, data_format: DataFormat, spectral_range: SpectralRange = None):
        super().__init__(params={"data_mode": data_mode, "data_format": data_format, "spectral_range": spectral_range})

    def prepare_message(self) -> Message:
        message_content = b'MEDR,' +  bytes(str(self.params["data_mode"].value), 'utf-8') + b','+ bytes(str(self.params["data_format"].value), 'utf-8') + b','
        
        if isinstance(self.params["data_mode"], DataMode.SPECTRAL_DATA) and self.params["spectral_range"]:
            message_content += bytes(str(self.params["spectral_range"].value), 'utf-8') + delimiter

        elif isinstance(self.params["data_mode"], DataMode.COLORIMETRIC_DATA):
            message_content += bytes(str(DataBlockNumber.COLORIMETRIC_DATA.value).zfill(2), 'utf-8') + delimiter

        else:
            message_content += bytes(str(DataBlockNumber.MEASUREMENT_CONDITIONS.value), 'utf-8') + delimiter

        return Message(params=self.params, message=message_content)
    
    async def send_message(self, msg: Message):
        try:
            self.exec_write(msg.message)
            resp1 = await [self.receive_message().decode("utf-8").replace('"OK00,', '').strip('"\n')]

            return resp1
        except Exception as err:
            raise Exception("An error occurred while sending data: ", err)

class ExecuteProgram:
    @classmethod
    async def run_program(cls, program: Union[list[Command], Command], save_file_name: str) -> None:
        connection = Connection.get_shared_connection()
        try:
            if isinstance(program, list):
                for command in program:
                    message = command.prepare_message()
                    response = await command.send_message(message)

                    builder = JsonBuilderFactory.create_builder(command.data_mode, save_file_name, response)
                    builder.build()
                    
            elif isinstance(program, Command):
                message = program.prepare_message()
                response = await program.send_message(message)

                builder = JsonBuilderFactory.create_builder(program.data_mode, save_file_name, response)
                builder.build()
            else:
                raise TypeError("Invalid program type. Must be a Command or a list of Commands.")
        except Exception as err: 
            print(f"An error occurred:", err)
        finally:
            cls.cleanup(connection)

    @classmethod
    def cleanup(cls, connection):
        if connection:
            connection.close()


class JsonBuilder:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.result_data = {}

    def build(self):
        json_structure = {self.__class__.__name__: self.result_data}
        data_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'data'))
        filename = f"{self.file_name}.json"
        file_path = os.path.join(data_folder, filename)

        if os.path.exists(file_path):
            with open(file_path, 'r') as existing_file:
                existing_data = json.load(existing_file)
            existing_data.update(json_structure)
            json_structure = existing_data

        with open(file_path, 'w', newline='') as jsonfile:
            json.dump(json_structure, jsonfile, indent=4)


class ColorimetricJsonBuilder(JsonBuilder):
    def __init__(self, file_name: str, data):
        super().__init__(file_name)
        self.colorimetric_keys = [
            "Le", "Lv", "X", "Y", "Z", "x", "y", "u'", "v'", "T", "delta uv", "lambda d", "Pe",
            "X10", "Y10", "Z10", "x10", "y10", "u'10", "v'10", "T10", "delta uv10", "lambda d10", "Pe10",
        ]
        self.result_data = {"Colorimetric Data": {}}
        for key, value in zip(self.colorimetric_keys, data):
            self.result_data["Colorimetric Data"][key] = {"value": value, "switch": 0}

class MeasurementJsonBuilder(JsonBuilder):
    def __init__(self, file_name: str, data):
        super().__init__(file_name)
        self.meascon_keys = [
            "Speed mode", "Sync mode", "Integration time", "Internal ND filter",
            "Optional close-up lens", "Optional external ND filter", "Measurement angle", "Calibration channel"
        ]
        self.result_data = {"Measurement Conditions": {}}
        for key, value in zip(self.meascon_keys, data):
            self.result_data["Measurement Conditions"][key] = {"value": value, "switch": 0}

class SpectralJsonBuilder(JsonBuilder):
    def __init__(self, file_name: str, spectral_range: str, data):
        super().__init__(file_name)
        self.result_data = {"Spectral data": {spectral_range: {"value": data, "switch": 0}}}

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
            raise ValueError("Invalid builder type")
