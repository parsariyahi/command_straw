import os
import json
import asyncio
import zmq.asyncio


class Conn:
    """A class to establish and manage a connection with a ZMQ socket"""

    def __init__(self, host: str, port: int) -> None:
        """
        Initialize a new connection with the specified host and port.

        Args:
            host (str): The host address to connect to.
            port (int): The port number to connect to.
        """
        self.port = port
        self.host = host

        # Create a new ZMQ async context and socket
        self._context = zmq.asyncio.Context()
        self._socket = self._context.socket(zmq.DEALER)

        # Connect the socket to the specified host and port
        self._socket.connect(f"tcp://{self.host}:{self.port}")

        # Create a new poller object and register the socket for polling
        self.poller = zmq.asyncio.Poller()
        self.poller.register(self._socket, zmq.POLLIN)

    async def send(self, command: dict) -> None:
        """
        Send a JSON-encoded command to the connected socket.

        Args:
            command (dict): The command to send to the socket as a dictionary.

        Returns:
            None
        """
        await self._socket.send_json(command)

    async def recieve(self) -> dict:
        """
        Receive a JSON-encoded response from the connected socket.

        Returns:
            dict: The response from the socket as a dictionary.
        """
        response = await self._socket.recv_json()
        return response

    def close(self) -> None:
        """Destroy the context to close the connection"""
        self._context.destroy()


class Client:
    """A class to represent a ZMQ client that sends commands and receives responses"""

    def __init__(self, host: str = "127.0.0.1", port: int = 5555) -> None:
        """
        Initialize a new ZMQ client with the specified host and port.

        Args:
            host (str): The host address to connect to.
            port (int): The port number to connect to.
        """
        # Initialize a new connection with the specified host and port
        self._conn = Conn(host, port)

        # Get the current event loop
        self._loop = asyncio.get_event_loop()

    def set_input_file(self, file_name: str) -> None:
        """
        Load a JSON-encoded command from a file.

        Args:
            file_name (str): The name of the file containing the command to load.

        Returns:
            None
        """
        current_path = os.path.dirname(__file__)
        json_file_path = os.path.join(current_path, file_name)

        with open(json_file_path) as file:
            self.command = json.loads(file.read())

    async def _run_command(self) -> None:
        """
        Send the loaded command to the connected socket.

        Returns:
            None
        """
        await self._conn.send(self.command)

    async def _get_result(self) -> dict:
        """
        Receive a response from the connected socket.

        Returns:
            dict: The response from the socket as a dictionary.
        """
        response = await self._conn.recieve()
        return response

    async def start(self) -> None:
        """
        Run the loaded command and print the resulting response.

        Returns:
            None
        """
        sockets = await self._conn.poller.poll(10)
        await self._run_command()
        result = await self._get_result()
        print(result)

    def close(self) -> None:
        """
        Close the connection by destroying the context.

        Returns:
            None
        """
        self._conn.close()
