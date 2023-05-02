# Command Straw

Command Straw is a Python Project that allows you to execute various types of commands using a simple and consistent interface. It provides a number of executer classes that can be used to execute different types of commands, as well as a factory class for creating executer objects based on command types.

## Installation

To install Command Straw, simply clone the repository :

```bash
git clone https://github.com/parsariyahi/command_straw.git
```

Sure, here's an updated version of the usage section where the code is replaced with JSON:

## Usage

Here's an example of how to use Command Straw to execute a mathematical expression:

```json
{
    "command_type": "compute",
    "expression": "2 + 2"
}
```

You can also use Command Straw to execute operating system commands:

```json
{
    "command_type": "os",
    "command_name": "ls",
    "parameters": ["-la"]
}
```

To send a command to a Command Straw server, you first need to create a client object:

```python
import sys
import asyncio
from client import Client

if __name__ == "__main__":
    # Prompt the user to enter the file name to be processed.
    file_name = input("Enter Your File Name: ")
    # Create a new client instance with the specified IP address and port number.
    client = Client("127.0.0.1", 5555)
    # Set the input file for the client to the specified file name.
    client.set_input_file(file_name)
    # Start the client processing in an asynchronous event loop.
    asyncio.run(client.start())
```

### Client Side

The client side of Command Straw is responsible for sending commands to a Command Straw server and receiving the results. It provides a simple interface for creating and sending commands, as well as handling any errors that may occur.

#### Creating a Command

To create a command, simply create a dictionary with the necessary fields for the type of command you want to execute. For example, if you want to execute an operating system command, you might create a command like this:

```python
command = {
    "command_type": "os",
    "command_name": "ls",
    "parameters": ["-la"],
}
```

This specifies that we want to execute an operating system command (`command_type: "os"`) with the name `ls` and the parameters `["-la"]`.

For a mathematical expression, you might create a command like this:

```python
command = {
    "command_type": "compute",
    "expression": "2 + 2",
}
```

This specifies that we want to evaluate a mathematical expression (`command_type: "compute"`) with the expression `"2 + 2"`.

## Contributing

If you'd like to contribute to Command Straw, please fork the repository and make your changes on a feature branch. Once you've made your changes, submit a pull request and we'll review your changes as soon as possible.

## License

Command Straw is licensed under the MIT license. See [LICENSE](LICENSE) for more information.