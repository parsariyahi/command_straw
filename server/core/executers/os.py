import subprocess


class OSExecuter:

    @classmethod
    async def execute(cls, command):
        command = await cls._clean_command_to_execute(command)

        output = await cls._async_run(command)

        if output.returncode: # If return code is NonZero
            result = output.stderr
        else :
            result = output.stdout

        command = await cls._join_command_args(command)
        response = await cls._clean_data_for_response(command, result)

        return response

    @classmethod
    async def _async_run(cls, command) :
        output = subprocess.run(command, shell=True, 
                                capture_output=True, text=True)
        return output


    @classmethod
    async def _clean_command_to_execute(cls, command) :
        actual_command = command["command_name"]
        args = command["parameters"]

        return [actual_command] + args

    @classmethod
    async def _join_command_args(cls, command_args) :
        return " ".join(command_args)

    @classmethod
    async def _clean_data_for_response(cls, command, result):
        return {
            "given_os_command": command,
            "result": result,
        }