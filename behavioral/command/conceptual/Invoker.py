from Command import Command

class Invoker:
    def __init__(self) -> None:
        self.__on_start: Command|None = None
        self.__on_finish: Command|None = None

    def set_on_start(self, command: Command) -> None:
        self.__on_start = command

    def set_on_finish(self, command: Command) -> None:
        self.__on_finish = command

    def do_something_important(self) -> None:
        print("Invoker: Does anybody want something done before I begin?")

        if isinstance(self.__on_start, Command):
            self.__on_start.execute()
        
        print("Invoker: ...doing something really important...")

        print("Invoker: Does anybody want something done after I finish?")

        if isinstance(self.__on_finish, Command):
            self.__on_finish.execute()