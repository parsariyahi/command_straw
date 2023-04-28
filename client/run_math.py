import sys
import asyncio
import os, json
from client import Client

def run_commnad():

    command = {
        "command_type": "compute",
        "expression": "(2 + 2) * 10",
    }

    for i in range(0, 100):
        client = Client(command)

        resp = client.run_command()

        print(resp)

def main():
    run_commnad()

if __name__ == "__main__" :
    if "win" in sys.platform:
        # If the client is running windows we should add this.
        # RuntimeWarning: Proactor event loop does not implement add_reader family of methods required for zmq.
        # Registering an additional selector thread for add_reader support via tornado.
        # Use `asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())` to avoid this warning.
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    main()