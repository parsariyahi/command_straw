from .os import OSExecuter
from .math import MathExeciter

class ExecuterFactory:

    @staticmethod
    def get_executer(command_type):
        executers = {
            "os": OSExecuter,
            "compute": MathExeciter,
        }

        return executers.get(command_type, None)