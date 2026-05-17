from Middleware import Middleware
from time import time
import sys

class ThrottlingMiddleware(Middleware):
    def __init__(self, request_per_minute: int) -> None:
        self.__request_per_minute = request_per_minute
        self.__current_time = time()
        self.__request = 0

    def check(self, email: str, password: str) -> bool:
        if time() > self.__current_time + 60:
            self.__request = 0
            self.__current_time = time()

        self.__request += 1

        if self.__request > self.__request_per_minute:
            print("ThrottlingMiddleware: Request limit exceeded!")
            sys.exit()

        return super().check(email, password)