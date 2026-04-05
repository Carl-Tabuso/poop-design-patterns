from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from Property import Property

class HouseBuilder(ABC):
    @abstractmethod
    def build_walls(self) -> None:
        pass

    @abstractmethod
    def build_doors(self) -> None:
        pass

    @abstractmethod
    def build_windows(self) -> None:
        pass

    @abstractmethod
    def build_roof(self) -> None:
        pass

    @abstractmethod
    def build_garage(self) -> None:
        pass

    @abstractmethod
    def get_result() -> Property:
        pass