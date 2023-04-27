import sys
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
        self._socket = self._context.socket(zmq.REQ)
        self._socket.connect(
            "tcp://{}:{}".format(self.host, self.port)
        )

    async def send(self, command):
        await self._socket.send_json(command)

    async def recieve(self) :
        resp = await self._socket.recv_json()

        return resp

    def close(self):
        self._context.destroy()



class Client:

    def __init__(self, command: dict) -> None:
        self.command = command
        self._conn = Conn("localhost", 5555)
        self.loop = asyncio.get_event_loop()

    def run_command(self):
        return self.loop.run_until_complete(self.__async_run_command())

    async def __async_run_command(self):
        await self._conn.send(self.command)
        return await self._conn.recieve()

    def close(self):
        self._conn.close()