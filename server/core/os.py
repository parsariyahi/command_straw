class OSExecuter:

    @classmethod
    def execute(cls, command):
        command = cls._clean_command_to_execute(command)

        command = cls._clean_command_for_result(command)

        result = "some"

        response = cls._clean_data_for_response(command, result)

        return response

    @classmethod
    def _clean_command_to_execute(cls, command) :
        pass

    @classmethod
    def _clean_command_for_result(cls, command) :
        pass

    @classmethod
    def _clean_data_for_response(cls, command, result):
        return {
            "given_os_command": command,
            "result": result,
        }