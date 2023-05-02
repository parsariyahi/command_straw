import sys
import asyncio
from client import Client

if __name__ == "__main__":
    # Check if the OS platform is Windows and set the event loop policy accordingly to avoid RuntimeWarning.
    if "win" in sys.platform:
        # If the client is running on Windows, we should use the WindowsProactorEventLoopPolicy event loop policy.
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

    # Prompt the user to enter the file name to be processed.
    file_name = input("Enter Your File Name: ")

    # Create a new client instance with the specified IP address and port number.
    client = Client("127.0.0.1", 5555)

    # Set the input file for the client to the specified file name.
    client.set_input_file(file_name)

    # Start the client processing in an asynchronous event loop.
    asyncio.run(client.start())