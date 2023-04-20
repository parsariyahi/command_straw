import sys
import asyncio
from conn import Conn


if "win" in sys.platform:
    # RuntimeWarning: Proactor event loop does not implement add_reader family of methods required for zmq.
    # Registering an additional selector thread for add_reader support via tornado.
    # Use `asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())` to avoid this warning.
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class Client:

    def __init__(self, command) -> None:
        self.command = command
        self._conn = Conn("localhost", 5555)
        self.loop = asyncio.get_event_loop()

    def run_command(self):
        return self.loop.run_until_complete(self.__async_run_command())

    def close(self):
        self._conn.close()

    async def __async_run_command(self):
        await self._conn.send(self.command)
        return await self._conn.recieve()