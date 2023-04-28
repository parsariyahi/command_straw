from .executers import (
    OSExecuter,
    MathExecuter,
)


class ExecuterFactory:

    @staticmethod
    async def get_executer(command_type):
        executers = {
            "os": OSExecuter,
            "compute": MathExecuter,
        }

        return executers.get(command_type, None)