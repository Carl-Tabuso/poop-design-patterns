from Subject import Subject
from random import randint
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Observer import Observer

class ConcreteSubject(Subject):
    def __init__(self) -> None:
        self.state: int | None = None
        self.__observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        if observer not in self.__observers:
            self.__observers.append(observer)
            print("Subject: Attached an observer.")

    def detach(self, observer: Observer) -> None:
        if observer in self.__observers:
            self.__observers.remove(observer)
            print("Subject: Detached an observer.")

    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self.__observers:
            observer.update(self)

    def some_business_logic(self) -> None: 
        print("Subject: I'm doing something important.")
        self.state = randint(0, 10)

        print(f"Subject: My state has just changed to: {self.state}")
        self.notify()