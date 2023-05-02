import sys
import asyncio

from server import Server


if __name__ == "__main__":
    # Add WindowsProactorEventLoopPolicy if running on Windows to avoid a warning.
    if "win" in sys.platform:
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

    # Create a new ZMQ server and start it using asyncio.run()
    server = Server("*", 5555)
    asyncio.run(server.listen())