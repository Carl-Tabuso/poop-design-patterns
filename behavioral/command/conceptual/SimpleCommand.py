from Command import Command

class SimpleCommand(Command):
    def __init__(self, payload: str) -> None:
        self.__payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: See, I can do simple things like printing (\"{self.__payload}\")")