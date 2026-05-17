from Handler import Handler

class AbstractHandler(Handler):
    def __init__(self) -> None:
        self.__next_handler = None

    def set_next(self, handler: Handler) -> Handler:
        self.__next_handler = handler

        return handler
    
    def handle(self, request: str) -> None|str:
        if self.__next_handler:
            return self.__next_handler.handle(request)
        
        return None