from AbstractHandler import AbstractHandler

class SquirrelHandler(AbstractHandler):
    def handle(self, request: str) -> None|str:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}."
        else:
            return super().handle(request)