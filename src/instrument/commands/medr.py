from ..commands.command import Command, DELIMITER
from ..message import Message
from ..config.enums import DataBlockNumber, DataFormat, DataMode, SpectralRange
from ..receiver import Receiver


class MEDR(Command):
    def __init__(self, data_mode: DataMode, data_format: DataFormat, spectral_range: SpectralRange = None):
        super().__init__(params={"data_mode": data_mode, "data_format": data_format, "spectral_range": spectral_range})

    def prepare_message(self) -> Message:
        message_content = b'MEDR,' +  bytes(str(self.params["data_mode"].value), 'utf-8') + b','+ bytes(str(self.params["data_format"].value), 'utf-8') + b','

        if self.params["data_mode"] in SpectralRange:
                    message_content = b'MEDR,' +  bytes(str(1), 'utf-8') + b','+ bytes(str(self.params["data_format"].value), 'utf-8') + b','+ bytes(str(self.params["data_mode"].value), 'utf-8') + DELIMITER

        elif self.params["data_mode"] == DataMode.COLORIMETRIC_DATA:
            message_content += bytes(str(DataBlockNumber.COLORIMETRIC_DATA.value), 'utf-8') + DELIMITER

        elif self.params["data_mode"] == DataMode.MEASUREMENT_CONDITIONS:
            message_content += bytes(str(DataBlockNumber.MEASUREMENT_CONDITIONS.value), 'utf-8') + DELIMITER

        return Message(params=self.params, message=message_content)

    async def send_message(self, msg: Message, receiver: Receiver):
        try:
            self.exec_write(msg.message)

            resp1 = await receiver.receive_message()

            return resp1
        except Exception as err:
            raise Exception("An error occurred while sending data: ", err)