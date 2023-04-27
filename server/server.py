import asyncio
import zmq.asyncio

from core.executer import Executer

class Conn:

    def __init__(
        self,
        host: str,
        port: int,
    ) -> None:
        self.port = port
        self.host = host
        self._context = zmq.asyncio.Context()
        self._socket = self._context.socket(zmq.REP)
        self._socket.bind(
            "tcp://{}:{}".format(self.host, self.port)
        )

    async def send(self, result):
        await self._socket.send_json(result)

    async def recieve(self) :
        resp = await self._socket.recv_json()

        return resp

    def close(self):
        self._context.destroy()


class Server:
    def __init__(self) -> None:
        self._conn = Conn('*', 5555)
        self._loop = asyncio.get_event_loop()

    async def __async_read_command(self) :
        data = await self._conn.recieve()

        return data

    async def __async_send_response(self, response):
        await self._conn.send(response)
    
    async def _main(self):
        while True:
            command = await self.__async_read_command()

            response = Executer.execute(command)

            await self.__async_send_response(response)

    def start(self) :
        asyncio.ensure_future(
            self._main()
        )
        self._loop.run_forever()