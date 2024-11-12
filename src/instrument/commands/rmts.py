from ..commands.command import Command, DELIMITER
from ..message import Message
from ..config.enums import ModeSelect
from ..receiver import Receiver

class RMTS(Command):
    def __init__(self, switch: ModeSelect = ModeSelect.ENABLED):
        super().__init__(params={"switch": switch})

    def prepare_message(self) -> Message:
        message_content = b'RMTS,' + bytes(str(self.params["switch"].value), 'utf-8') + DELIMITER
        return Message(params=self.params, message=message_content)

    async def send_message(self, msg: Message, receiver: Receiver):
        try:
            self.exec_write(msg.message)

            resp1 = await receiver.receive_message()
            return resp1
        except Exception as err:
            raise Exception("An error occurred while sending data: ", err)
