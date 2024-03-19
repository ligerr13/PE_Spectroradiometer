from abc import ABC, abstractmethod
from src.instrument.message import Message
from src.instrument.connection import Connection

delimiter = b'\n'
ser = Connection()
ser.open()

class Command(ABC):
    @abstractmethod
    def send_message(self, msg: Message) -> bytes:
        """
        Sends a message to the instrument.

        Args:
            message (bytes): The message to be sent.
        """
        pass

    @abstractmethod
    def receive_message(self) -> None:
        """
        Receives message from the instrument.

        Returns:
            bytes: The received message.
        """
        pass   

class _RMTS(Command):
    def __init__(self):
        self.params = {"param": 1}

    def prepare_message(self) -> Message:
            message_content = b'RMTS,' + bytes(str(self.params["param"]), 'utf-8') + delimiter
            return Message(params=self.params, message=message_content)

    
    def send_message(self, msg: Message) -> bytes:
        if (0 <= msg.params["param"] <= 1):
            try:
                ser.serial_port.write(msg.message)
                return self.receive_message()
            except Exception as e:
                print("Error occurred while sending message:", str(e))
        else:
            raise ValueError("Invalid value! The value must be 0 or 1.")
    
    def receive_message(self) -> bytes:
        return ser.serial_port.read()


basic_measure_program = [
    _RMTS,
]

def run_program(program: list[Command]) -> None:
    for command in program:
        message = command.prepare_message()
        response = command.send_message(message)
        
        print(response)


run_program(basic_measure_program)