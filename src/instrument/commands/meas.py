from ..commands.command import Command
from ..message import Message
from ..config.enums import ModeSelect
from ..receiver import Receiver

class MEAS(Command):
    def __init__(self, switch: ModeSelect = ModeSelect.ENABLED):
        super().__init__(params={"switch": switch})

    def prepare_message(self) -> Message:
        message_content = b'MEAS,' + bytes(str(self.params["switch"].value), 'utf-8') + Command.DELIMITER
        return Message(params=self.params, message=message_content)

    async def send_message(self, msg: Message, receiver: Receiver):
        try:
            self.exec_write(msg.message)

            resp1 = await receiver.receive_message()
            resp2 = await receiver.receive_message()

            return resp1, resp2
        except Exception as err:
            print("An error occurred while sending data: ", err)