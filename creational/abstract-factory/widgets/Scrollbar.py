from abc import ABC, abstractmethod

class Scrollbar(ABC):
    @abstractmethod
    def scroll(self) -> str:
        pass

    @abstractmethod
    def render(self) -> str:
        pass

    def __str__(self) -> str:
        return "Scrollbar"
