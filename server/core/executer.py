import subprocess

from .factory import ExecuterFactory

class Executer:

    @classmethod
    def execute(cls, command):
        executer = ExecuterFactory.get_executer(command["command_type"])

        result = executer.execute(command)

        return result