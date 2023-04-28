from .factory import ExecuterFactory

class Executer:

    @classmethod
    async def execute(cls, command):
        executer = await ExecuterFactory.get_executer(command["command_type"])

        result = await executer.execute(command)

        return result