import os
import json
import asyncio
import zmq.asyncio

class Conn:

    def __init__(
        self,
        host: str,
        port: int,
    ) -> None:
        self.port = port
        self.host = host
        self._context = zmq.asyncio.Context()
        self._socket = self._context.socket(zmq.DEALER)
        self._socket.connect(
            "tcp://{}:{}".format(self.host, self.port))
        self.poller = zmq.asyncio.Poller()
        self.poller.register(self._socket, zmq.POLLIN)

    async def send(self, command):
        await self._socket.send_json(command)

    async def recieve(self) :
        response = await self._socket.recv_json()

        return response

    def close(self):
        self._context.destroy()



class Client:

    def __init__(self, host="127.0.0.1", port=5555) -> None:
        self._conn = Conn(host, port)
        self._loop = asyncio.get_event_loop()

    def set_input_file(self, file_name):
        current_path = os.path.dirname(__file__)
        json_file_path = os.path.join(current_path, file_name)

        with open(json_file_path) as file:
            self.command = json.loads(file.read())

    async def _run_command(self):
        await self._conn.send(self.command)

    async def _get_result(self):
        response = await self._conn.recieve()
        return response

    async def start(self):
        sockets = await self._conn.poller.poll(10)
        await self._run_command()
        result = await self._get_result()
        print(result)

    def close(self):
        self._conn.close()