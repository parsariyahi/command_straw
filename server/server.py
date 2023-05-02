import json
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
        self._socket = self._context.socket(zmq.ROUTER)
        self._socket.bind(
            "tcp://{}:{}".format(self.host, self.port)
        )
        self.poller = zmq.asyncio.Poller()
        self.poller.register(self._socket, zmq.POLLIN)

    async def send(self, uid, result):
        response = json.dumps(result, indent=2).encode("utf-8")
        await self._socket.send_multipart((uid, response))

    async def recieve(self) :
        uid, request = await self._socket.recv_multipart()

        return uid, request

    def close(self):
        self._context.destroy()


class Server:
    def __init__(self, host="*", port=5555) -> None:
        self._conn = Conn(host, port)
        self._loop = asyncio.get_event_loop()

    async def _execute_command(self, command):
        response = await Executer.execute(command)
        return response

    async def _request_handler(self, uid, request):
        command = json.loads(request.decode())
        print(f"command is: {command}")
        result = await self._execute_command(command)
        print(f"result is: {result}")
        await self._conn.send(uid, result)

    async def listen(self):
        while True:
            print("listening")
            socks = dict(await self._conn.poller.poll())
            print(socks)

            if self._conn._socket in socks:
                uid, request = await self._conn.recieve()
                print(request, uid)
                asyncio.create_task(self._request_handler(uid, request))