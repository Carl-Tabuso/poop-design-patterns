from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from Scrollbar import Scrollbar
    from Window import Window

class WidgetFactory(ABC):
    @abstractmethod
    def create_scrollbar(self) -> Scrollbar:
        pass

    @abstractmethod
    def create_window(self) -> Window:
        pass

    def __str__(self) -> str:
        return "WidgetFactory"
