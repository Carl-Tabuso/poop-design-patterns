from abc import ABC, abstractmethod

class WidgetFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_scrollbar():
        pass

    @staticmethod
    @abstractmethod
    def create_window():
        pass

    def __str__(self) -> str:
        return "WidgetFactory"
