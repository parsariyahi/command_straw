import asyncio


class OSExecuter:

    @classmethod
    async def execute(cls, command):
        command = await cls._clean_command_to_execute(command)
        command_str = await cls._build_command(command)
        proc = await asyncio.subprocess.create_subprocess_shell(
                command_str, stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE)

        stdout = await proc.stdout.read()

        result = await cls._clean_data_for_response(command_str, stdout.decode())

        return result

    @classmethod
    async def _clean_command_to_execute(cls, command) :
        actual_command = command["command_name"]
        args = command["parameters"]

        return [actual_command] + args

    @classmethod
    async def _build_command(cls, command_list) :
        return " ".join(command_list)

    @classmethod
    async def _clean_data_for_response(cls, command, stdout):
        return {
            "given_os_command": command,
            "result": stdout,
        }