from AbstractHandler import AbstractHandler

class DogHandler(AbstractHandler):
    def handle(self, request: str) -> None|str:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}."
        else:
            return super().handle(request)