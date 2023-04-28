import sys
import asyncio
import os, json
from client import Client

def get_file_path() :

    # Get json file name and generate the path
    json_file_name =  input("Enter your json file name: ")
    current_path = os.path.dirname(__file__)
    json_file_path = os.path.join(current_path, json_file_name)

    with open(json_file_path) as file:
        command = json.loads(
            file.read()
        )

    cl = Client(command)
    for i in range(0, 1) :
        resp = cl.run_command()
        print(resp)

def run_commnad():

    command = {
        "command_type": "os",
        "command_name": "ping",
        "parameters": [
            "127.0.0.1",
            "-n",
            "6",
        ]
    }

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