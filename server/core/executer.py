from .factory import ExecuterFactory

class CommandExecuter:
    """
    A class for executing commands using various executer classes.
    """

    @classmethod
    async def execute(cls, command: dict) -> dict:
        """
        Execute the specified command using an appropriate executer class and return the result.

        Args:
            command (dict): A dictionary representing the command to execute.

        Returns:
            A dictionary representing the result of the command execution.
        """
        executer = await ExecuterFactory.get_executer(command["command_type"])

        result = await executer.execute(command)

        return result