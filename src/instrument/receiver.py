from .connection import Connection 

class Receiver:
    def __init__(self, *args, **kwargs):
        self.connection = Connection.get_shared_connection()

    """
    Receives the incomming message.
    """
    async def receive_message(self) -> str:

        """
        Receives message from the instrument.

        Returns:
            str: The received message.
        """
        try:
            return self.connection.readline().decode("utf-8").replace('OK00,', '').strip('\n')
        except Exception as err:
            raise Exception("An error occurred while reading data: ", err)