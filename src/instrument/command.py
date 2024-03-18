from abc import ABC, abstractmethod
from message import Message
from connection import Connection
import asyncio

delimiter = b'\n'
ser = Connection()
ser.open()

class Command(ABC):
    def __init__(self, *args, **kwargs):
        if not ser or not ser.open:
                raise ValueError("Communication cannot be performed without an open connection.")

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
            return ser.serial_port.read()
        except Exception as err:
            raise ValueError("An error occurred while reading data: ", err)

        

class RMTS(Command):
    def __init__(self, switch):
        super().__init__(params={"switch": switch})


    def prepare_message(self) -> Message:
        message_content = b'RMTS,' + bytes(str(self.params["switch"]), 'utf-8') + delimiter
        return Message(params=self.params, message=message_content)
    
    async def send_message(self, msg: Message) -> bytes:
        try:
            ser.serial_port.write(msg.message)
            resp1 = await self.receive_message()
            return resp1
        except Exception as err:
            raise ValueError("An error occurred while sending data: ", err)

            
class MSWE(Command):
    def __init__(self, switch):
        super().__init__(params={"switch": switch})


    def prepare_message(self) -> Message:
        message_content = b'MSWE,' + bytes(str(self.params["switch"]), 'utf-8') + delimiter
        return Message(params=self.params, message=message_content)
    
    async def send_message(self, msg: Message) -> bytes:
        try:
            ser.serial_port.write(msg.message)
            resp1 = await self.receive_message()
            return resp1
        except Exception as err:
            raise ValueError("An error occurred while sending data: ", err)


class MEAS(Command):
    def __init__(self, switch):
        super().__init__(params={"switch": switch})


    def prepare_message(self) -> Message:
        message_content = b'MEAS,' + bytes(str(self.params["switch"]), 'utf-8') + delimiter
        return Message(params=self.params, message=message_content)
    
    async def send_message(self, msg: Message) -> bytes:
        try:
            ser.serial_port.write(msg.message)  
            resp1 = await self.receive_message()
            resp2 = await self.receive_message()
            return resp1, resp2
        except Exception as err:
            raise ValueError("An error occurred while sending data: ", err)



#TODO PROGRAMM CLASS 
        #OPEN CLOSE CONENCTION
        #ASYNC RUN PROGRAM

basic_measure_program = [ 
    RMTS(1),
    MSWE(0),
    MEAS(1)
]


async def run_program(program: list[Command]) -> None:
    for command in program:
        message = command.prepare_message()
        response = await command.send_message(message)
        
        print(response)


asyncio.run(run_program(basic_measure_program))