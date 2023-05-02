import asyncio

from .base import Executer


class OSExecuter(Executer):
    """
    An executer class for running operating system commands.
    """

    @classmethod
    async def execute(cls, command: dict) -> dict:
        """
        Execute the specified operating system command and return the result.

        Args:
            command (dict): A dictionary representing the command to execute.

        Returns:
            A dictionary representing the result of the command execution.
        """
        command = await cls._clean_command_to_execute(command)
        command_str = await cls._build_command(command)
        proc = await asyncio.subprocess.create_subprocess_shell(
                command_str, stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE)

        stdout = await proc.stdout.read()

        result = await cls._clean_data_for_response(command_str, stdout.decode())

        return result

    @classmethod
    async def _clean_command_to_execute(cls, command: dict) -> list:
        """
        Clean up the command parameters and return them as a list.

        Args:
            command (dict): A dictionary representing the command to execute.

        Returns:
            A list containing the cleaned up command parameters.
        """
        actual_command = command["command_name"]
        args = command["parameters"]

        return [actual_command] + args

    @classmethod
    async def _build_command(cls, command_list: list) -> str:
        """
        Build a shell command string from the given list of command parameters.

        Args:
            command_list (list): A list of command parameters.

        Returns:
            A string representing the shell command to execute.
        """
        return " ".join(command_list)

    @classmethod
    async def _clean_data_for_response(cls, command: str, stdout: str) -> dict:
        """
        Clean up the command and output data and return them as a dictionary.

        Args:
            command (str): The original command that was executed.
            stdout (str): The standard output of the command execution.

        Returns:
            A dictionary containing the cleaned up command and output data.
        """
        return {
            "given_os_command": command,
            "result": stdout,
        }
