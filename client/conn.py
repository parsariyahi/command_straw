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
    
    async def __aenter__(self):
        self._socket = self._context.socket(zmq.REQ)
        self._socket.connect(
            "tcp://{}:{}".format(self.host, self.port)
        )
        return self

    async def __aexit__(self, *args, **kwargs):
        self._socket.close()

    async def send(self, command):
        await self._socket.send_json(command)

    async def recieve(self) :
        resp = await self._socket.recv_json()

        return resp
