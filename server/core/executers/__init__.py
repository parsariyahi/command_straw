from .os import OSExecuter
from .math import MathExecuter
from .base import Executer


__all__ = [
    "Executer",
    "OSExecuter",
    "MathExecuter",
]


"""
This module defines a number of executer classes for different types of commands.

Classes:
- Executer: An abstract base class for defining executable commands.
- OSExecuter: A class for executing operating system commands.
- MathExecuter: A class for executing simple mathematics commands.
"""


# No further implementation is required, as this file is only used for exporting
# the classes defined in other modules.