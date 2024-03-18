from abc import ABC, abstractmethod
from message import Message
from connection import Connection
import asyncio
from enum import Enum
from statemachine import StateMachine, State

delimiter = b'\n'

class CommandState(Enum):
    STARTED = 1
    IN_PROGRESS = 2
    ENDED = 3

class StateMachine(StateMachine):
    started = State(CommandState.STARTED, initial=True)
    in_progress = State(CommandState.IN_PROGRESS)
    ended = State(CommandState.ENDED)

    start_to_in_progress = started.to(in_progress)
    in_progress_to_ended = in_progress.to(ended)

class Command(ABC):
    def __init__(self, *args, **kwargs):
        self.connection = Connection.get_shared_connection()

        if not self.connection:
            raise ValueError("Communication cannot be performed without an open connection or Connection object is not valid.")
        if args:
            self.params = args[0]
        else:
            self.params = kwargs.get('params', {})

        self.state = StateMachine()

    @abstractmethod
    def prepare_message(self) -> Message:

        """
        Prepares the message.

        Returns:
            bytes: The received message.
        """
        pass

    @abstractmethod
    async def send_message(self, msg: Message) -> bytes:

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
            raise ValueError("An error occurred while reading data: ", err)
        
    
    def exec_write(self, message: str) -> None:
        self.connection.write(message)


class RMTS(Command):
    def __init__(self, switch):
        if not isinstance(switch, int) or not (0 or 1):
            raise ValueError("Parameter 'switch' must be an integer 0 or 1.")
        super().__init__(params={"switch": switch})


    def prepare_message(self) -> Message:
        message_content = b'RMTS,' + bytes(str(self.params["switch"]), 'utf-8') + delimiter
        return Message(params=self.params, message=message_content)
    
    async def send_message(self, msg: Message) -> bytes:
        try:
            self.state.start_to_in_progress()
            self.exec_write()

            resp1 = await self.receive_message()
            return resp1
        except Exception as err:
            raise ValueError("An error occurred while sending data: ", err)
        finally:
            self.state.in_progress_to_ended()

    
class MSWE(Command):
    def __init__(self, switch):
        if not isinstance(switch, int) or not (0 or 1):
            raise ValueError("Parameter 'switch' must be an integer 0 and 1.")
        super().__init__(params={"switch": switch})


    def prepare_message(self) -> Message:
        message_content = b'MSWE,' + bytes(str(self.params["switch"]), 'utf-8') + delimiter
        return Message(params=self.params, message=message_content)
    
    async def send_message(self, msg: Message) -> bytes:
        try:
            self.state.start_to_in_progress()
            self.exec_write(msg.message)

            resp1 = await self.receive_message()
            return resp1
        except Exception as err:
            raise ValueError("An error occurred while sending data: ", err)
        finally:
            self.state.in_progress_to_ended()


class MEAS(Command):
    def __init__(self, switch):
        if not isinstance(switch, int) or not (0 or 1):
            raise ValueError("Parameter 'switch' must be an integer 0 or 1.")
        super().__init__(params={"switch": switch})


    def prepare_message(self) -> Message:
        message_content = b'MEAS,' + bytes(str(self.params["switch"]), 'utf-8') + delimiter
        return Message(params=self.params, message=message_content)
    
    async def send_message(self, msg: Message) -> bytes:
        try:
            self.state.start_to_in_progress()
            self.exec_write(msg.message)
            
            resp1 = await self.receive_message()
            resp2 = await self.receive_message()

            return resp1, resp2
        except Exception as err:
            raise ValueError("An error occurred while sending data: ", err)
        finally:
            self.state.in_progress_to_ended()


class MEDR(Command):
    def __init__(self, data_mode: int, data_format: int, data_block_number_to_read: int):

        if not (0 <= data_mode <= 2):
            raise ValueError("Parameter 'data_mode' must be an integer between 0 and 2.")
        
        if data_format not in (0, 1):
            raise ValueError("Parameter 'data_format' must be an integer, 0 or 1.")
        
        if data_mode == 0:
            if data_block_number_to_read != 1:
                raise ValueError("Parameter 'data_block_number_to_read' must be an integer 1")
        elif data_mode == 1:
            if not 1 <= data_block_number_to_read <= 4:
                raise ValueError("Parameter 'data_block_number_to_read' must be in the range of 1 to 4.")
        elif data_mode == 2:
            if not ((0 <= data_block_number_to_read <= 5) or (11 <= data_block_number_to_read <= 15) or
                    (data_block_number_to_read == 100) or (data_block_number_to_read == 101)):
                raise ValueError("Parameter 'data_block_number_to_read' must be in the range of 00 to 05, 11 to 15, or equal to 100 or 101.")
        
        super().__init__(params={"data_mode": data_mode, "data_format": data_format, "data_block_number_to_read": data_block_number_to_read})

    def prepare_message(self) -> Message:
        message_content = b'MEDR,' +  bytes(str(self.params["data_mode"]), 'utf-8') + b','+ bytes(str(self.params["data_format"]), 'utf-8') + b','  + bytes(str(self.params["data_block_number_to_read"]).zfill(2), 'utf-8') + delimiter
        return Message(params=self.params, message=message_content)
    
    async def send_message(self, msg: Message) -> bytes:
        try:
            self.state.start_to_in_progress()
            self.exec_write(msg.message)
            
            resp1 = await [self.receive_message().decode("utf-8").replace('"OK00,', '').strip('"\n')]

            return resp1
        except Exception as err:
            raise ValueError("An error occurred while sending data: ", err)
        finally:
            self.state.in_progress_to_ended()


class ExecuteProgram():
    def __init__(self):
        self.state = StateMachine()
        self.connection = Connection.get_shared_connection()

    @classmethod
    async def run_program(cls, program: list[Command]) -> None:
        state = StateMachine()
        connection = Connection.get_shared_connection()
        
        state.start_to_in_progress()
        try:
            for command in program:
                message = command.prepare_message()
                response = await command.send_message(message)

                print(response)
        except Exception as e: 
            print(f"An error occurred: {e}")
        finally:
            state.in_progress_to_ended()
            cls.cleanup(connection)

    @classmethod
    def cleanup(cls, connection):
        if connection:
            connection.close()



basic_measure_program = [
    RMTS(switch = 1),
    MSWE(switch = 0),
    MEAS(switch = 1),
    MEDR(data_mode = 0, data_format = 0, data_block_number_to_read = 1),
  *[MEDR(data_mode=1, data_format=0, data_block_number_to_read=spectral_number) for spectral_number in range(1,5)],
    MEDR(data_mode = 2, data_format = 0, data_block_number_to_read = 0),
    RMTS(switch = 0)
]

asyncio.run(ExecuteProgram.run_program(basic_measure_program))