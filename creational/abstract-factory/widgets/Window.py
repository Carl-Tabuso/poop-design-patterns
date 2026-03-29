from abc import ABC, abstractmethod

class Window(ABC):
    @abstractmethod
    def resize(self) -> str:
        pass

    @abstractmethod
    def render(self) -> str:
        pass

    def __str__(self) -> str:
        return "Window"
