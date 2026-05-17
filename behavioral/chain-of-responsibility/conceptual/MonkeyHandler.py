from AbstractHandler import AbstractHandler

class MonkeyHandler(AbstractHandler):
    def handle(self, request: str) -> None|str:
        if request == "Banana":
            return f"Monkey: I'll eat the {request}."
        else:
            return super().handle(request)