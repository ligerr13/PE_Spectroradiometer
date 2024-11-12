from abc import ABC, abstractmethod
from ..message import Message
from ..connection import Connection
from ..config.enums import DataBlockNumber, DataFormat, DataMode, ModeSelect, SpectralRange
from typing import Union
from ..receiver import Receiver
from ...misc.json_util import JsonBuilderFactory

DELIMITER = b'\n'

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
    async def send_message(self, msg: Message, receiver: Receiver):

        """
        Sends a message to the instrument.

        Args:
            message (bytes): The message to be sent.
            receiver (Receiver): Receives the incoming data.
        """
        pass


    def exec_write(self, message: bytes) -> bytes:
        if not self.connection:
            self.connection = Connection.get_shared_connection()

        self.connection.write(message)

class ExecuteProgram:
    @classmethod
    async def run_program(cls, program: Union[list[Command], Command], save_file_name: str = None) -> None:
        connection = Connection.get_shared_connection()
        try:
            if isinstance(program, list):

                for command in program:
                    message = command.prepare_message()
                    response = await command.send_message(message)

                    if "data_mode" in command.params.keys() and save_file_name:
                        builder = JsonBuilderFactory.create_builder(command.params["data_mode"], save_file_name, response)

                        builder.build()

            elif isinstance(program, Command):
                message = program.prepare_message()
                response = await program.send_message(message)

                if save_file_name  and isinstance(program.params["data_mode"], DataMode):
                    builder = JsonBuilderFactory.create_builder(program.params["data_mode"], save_file_name, response)
                    builder.build()
            else:
                raise TypeError("Invalid program type. Must be a Command or a list of Commands.")
        except Exception as err:
            print(f"An error occurred: ", err.with_traceback())
        finally:
            cls.cleanup(connection)

    @classmethod
    def cleanup(cls, connection):
        if connection:
            connection.close()
