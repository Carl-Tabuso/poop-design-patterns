from Observer import Observer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Subject import Subject

class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject.state == 0 or subject.state >= 2:
            print("ConcreteObserverB: Reacted to the event.")
