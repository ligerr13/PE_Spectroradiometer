from .commands.command import Command
from .receiver import Receiver
from src.misc.json_util import JsonBuilderFactory


class Invoker:
    """
    Executes all commands added to the command list asynchronously, with an optional save feature.
    """

    def __init__(self, save_file: bool = False, save_options: dict = None):
        """
        Initialize the Invoker with optional saving parameters.
        
        Args:
            save_file (bool): Whether to save the output of each command.
            save_options (dict, optional): Options for saving, such as filename and format.
        """
        self._commands = []
        self._receiver = Receiver()
        self._save_file = save_file
        self._save_options = save_options or {}

    def set_save_file(self, save_file: bool, save_options: dict = None):
        """
        Set saving options after instantiation.
        
        Params:
            save_file: Whether to save the output of each command.
            save_options: Options for saving, such as filename and format.
        """
        self._save_file = save_file
        self._save_options = save_options or {}

    def add_command(self, command: Command):
        """
        Add a command to the command list.
        """
        self._commands.append(command)

    async def execute_commands(self) -> None:
        """
        Executes all commands asynchronously. If saving is enabled, it will save the response.
        """
        for command in self._commands:
            if isinstance(command, Command):
                message = command.prepare_message()
                response = await command.send_message(message, self._receiver)

                if self._save_file and "data_mode" in command.params and response:
                    filename = self._save_options.get("filename", "output.json")
                    builder = JsonBuilderFactory.create_builder(command.params["data_mode"], filename, response)
                    builder.build()