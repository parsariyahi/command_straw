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

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args, **kwargs):
        # self._socket.close()
        pass

    async def send(self, command):
        await self._socket.send_json(command)

    async def recieve(self) :
        resp = await self._socket.recv_json()

        return resp

    def close(self):
        self._context.destroy()
