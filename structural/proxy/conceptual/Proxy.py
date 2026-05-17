from Subject import Subject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from RealSubject import RealSubject

class Proxy(Subject):
    def __init__(self, real_subject: RealSubject) -> None:
        self.__real_subject = real_subject

    def request(self) -> None:
        if self.__check_access():
            self.__real_subject.request()
            self.__log_access()

    def __check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")

        return True;

    def __log_access(self) -> None:
        print("Proxy: Logging the time of request.")