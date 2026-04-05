from abc import ABC, abstractmethod

class Sofa(ABC):
    @abstractmethod
    def has_legs(self) -> bool:
        pass

    @abstractmethod
    def sit_on(self) -> str:
        pass