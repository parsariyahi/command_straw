import sys
import asyncio
import zmq.asyncio
from executer import Executer

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

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args, **kwargs):
        # self._socket.close()
        pass

    async def send(self, result):
        await self._socket.send_json(result)

    async def recieve(self) :
        resp = await self._socket.recv_json()

        return resp

    def close(self):
        self._context.destroy()

if "win" in sys.platform:
    # RuntimeWarning: Proactor event loop does not implement add_reader family of methods required for zmq.
    # Registering an additional selector thread for add_reader support via tornado.
    # Use `asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())` to avoid this warning.
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class Server:
    def __init__(self) -> None:
        self._conn = Conn('*', 5555)
        self._loop = asyncio.get_event_loop()

    def listen(self):
        self._loop.run_forever()
        print('asdkfjdsakjflksdjaf')

    def listen(self) :
        data = self._loop.create_task(
            self.__async_read_command()
        )

        return data

    async def __async_read_command(self) :
        data = await self._conn.recieve()

        return data

    async def __async_command_result(self, res):
        data = {
            'status': 'okj',
            'result': res
        }

        await self._conn.send(data)
    
    async def _main(self):
        while True:
            command = await self.__async_read_command()

            result = Executer.execute(command)

            await self.__async_command_result(result)

    def start(self) :
        asyncio.ensure_future(
            self._main()
        )
        self._loop.run_forever()