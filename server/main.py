import sys
import asyncio

from server import Server


def main() :
    server = Server()
    server._main()


if __name__ == "__main__":
    if "win" in sys.platform:
        # If the server is running on windows, we should add this.
        # RuntimeWarning: Proactor event loop does not implement add_reader family of methods required for zmq.
        # Registering an additional selector thread for add_reader support via tornado.
        # Use `asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())` to avoid this warning.
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    server = Server()
    asyncio.run(server.start())