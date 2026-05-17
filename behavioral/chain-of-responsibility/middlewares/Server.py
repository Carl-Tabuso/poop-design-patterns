from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Middleware import Middleware

class Server:
    def __init__(self) -> None:
        self.__users = {}
        self.__middleware = None

    def set_middleware(self, middleware: Middleware) -> None:
        self.__middleware = middleware

    def log_in(self, email: str, password: str) -> bool:
        if self.__middleware.check(email, password):
            print("Server: Authorization has been successful!")

            return True
        
        return False
    
    def register(self, email: str, password: str) -> None:
        self.__users[email] = password

    def has_email(self, email: str) -> bool:
        return email in self.__users
    
    def is_valid_password(self, email: str, password: str) -> bool:
        return self.__users[email] == password