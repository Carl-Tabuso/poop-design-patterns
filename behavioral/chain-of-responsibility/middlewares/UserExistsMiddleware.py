from Middleware import Middleware
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Server import Server

class UserExistsMiddleware(Middleware):
    def __init__(self, server: Server) -> None:
        self.__server = server

    def check(self, email: str, password: str) -> bool:
        if not self.__server.has_email(email):
            print("UserExistsMiddleware: This email is not registered!")

            return False
        
        if not self.__server.is_valid_password(email, password):
            print("UserExistsMiddleware: Wrong password!")

            return False
        
        return super().check(email, password)