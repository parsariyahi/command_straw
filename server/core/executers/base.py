from abc import ABC, abstractmethod


class Executer(ABC):
    """
    An abstract base class for defining executable commands.
    """

    @abstractmethod
    async def execute(self, *args, **kwargs) -> dict:
        """
        Execute the command and return the result as a dictionary.

        Args:
            args: Optional positional arguments for the command.
            kwargs: Optional keyword arguments for the command.

        Returns:
            A dictionary representing the result of the command execution.
        """
        raise NotImplementedError