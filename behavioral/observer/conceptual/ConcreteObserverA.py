from Observer import Observer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Subject import Subject

class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject.state < 3:
            print("ConcreteObserverA: Reacted to the event.")