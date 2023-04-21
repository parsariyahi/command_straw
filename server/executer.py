import subprocess


class Executer:

    @staticmethod
    def execute(command):
        res = subprocess.check_output(command['command_name'], shell=True)

        return res.decode()