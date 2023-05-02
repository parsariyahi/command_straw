import json
import asyncio
import zmq.asyncio

from core.executer import CommandExecuter


class Conn:
    """A class to establish and manage a connection with a ZMQ socket"""

    def __init__(self, host: str, port: int) -> None:
        """
        Initialize a new connection with the specified host and port.

        Args:
            host (str): The host address to bind to.
            port(int): The port number to bind to.
        """
        self.port = port
        self.host = host
        self._context = zmq.asyncio.Context()
        self._socket = self._context.socket(zmq.ROUTER)
        self._socket.bind(f"tcp://{self.host}:{self.port}")
        self.poller = zmq.asyncio.Poller()
        self.poller.register(self._socket, zmq.POLLIN)

    async def send(self, uid: bytes, result: dict) -> None:
        """
        Send a JSON-encoded response to the connected socket.

        Args:
            uid (bytes): The unique identifier for the request.
            result (dict): The response to the request.

        Returns:
            None
        """
        response = json.dumps(result, indent=2).encode("utf-8")
        await self._socket.send_multipart((uid, response))

    async def receive(self) -> tuple:
        """
        Receive a JSON-encoded request from the connected socket.

        Returns:
            tuple: A tuple containing the unique identifier and the request as a dictionary.
        """
        uid, request = await self._socket.recv_multipart()
        command = json.loads(request.decode())
        return uid, command

    def close(self) -> None:
        """Close the connection by destroying the context."""
        self._context.destroy()


class Server:
    """A class to represent a ZMQ server that listens for requests and sends responses."""

    def __init__(self, host="*", port=5555) -> None:
        """
        Initialize a new ZMQ server with the specified host and port.

        Args:
            host (str): The host address to bind to.
            port(int): The port number to bind to.
        """
        self._conn = Conn(host, port)
        self._loop = asyncio.get_event_loop()

    async def _execute_command(self, command: dict) -> dict:
        """Execute a command using an Executer object and return the result."""
        response = await CommandExecuter.execute(command)
        return response

    async def _request_handler(self, uid: bytes, request: dict) -> None:
        """Handle a request by executing a command and sending back the result."""
        result = await self._execute_command(request)
        await self._conn.send(uid, result)

    async def listen(self) -> None:
        """Listen for incoming requests and handle them asynchronously."""
        while True:
            sockets = dict(await self._conn.poller.poll())

            if self._conn._socket in sockets:
                uid, request = await self._conn.receive()
                asyncio.create_task(self._request_handler(uid, request))
