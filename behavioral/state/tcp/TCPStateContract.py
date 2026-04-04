from abc import ABC, abstractmethod

class TCPStateContract(ABC):
    @abstractmethod
    def open(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @abstractmethod
    def acknowledge(self) -> None:
        pass