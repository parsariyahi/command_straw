import sys
import asyncio
from client import Client

if __name__ == "__main__" :
    if "win" in sys.platform:
        # If the client is running windows we should add this.
        # RuntimeWarning: Proactor event loop does not implement add_reader family of methods required for zmq.
        # Registering an additional selector thread for add_reader support via tornado.
        # Use `asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())` to avoid this warning.
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

    file_name = input("Enter Your File Name: ")

    client = Client("127.0.0.1", 5555)
    client.set_input_file(file_name)
    asyncio.run(client.start())