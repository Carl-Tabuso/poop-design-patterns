from Command import Command
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Receiver import Receiver

class ComplexCommand(Command):
    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        self.__receiver = receiver
        self.__a = a
        self.__b = b

    def execute(self) -> None:
        print("ComplexCommand: Complex stuff should be done by a receiver object.")
        
        self.__receiver.do_something(self.__a)
        self.__receiver.do_something_else(self.__b)