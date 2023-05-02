from typing import Type, Optional

from .executers import Executer, OSExecuter, MathExecuter


class ExecuterFactory:
    """
    A factory class for creating executer objects based on a command type.
    """

    @staticmethod
    async def get_executer(command_type: str) -> Optional[Type[Executer]]:
        """
        Create and return an executer object based on the command type.

        Args:
            command_type (str): The type of the command to execute.

        Returns:
            An instance of an executer object corresponding to the given command type, or None if the
            command type is not supported.
        """
        executers = {
            "os": OSExecuter,
            "compute": MathExecuter,
        }

        return executers.get(command_type.lower(), None)
