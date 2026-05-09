from abc import ABC, abstractmethod

class InputFormat(ABC):
    @abstractmethod
    def format_text(self, text: str) -> str:
        pass