from abc import ABC, abstractmethod

class Builder(ABC):
    @abstractmethod
    def reset(self) -> Builder:
        pass

    @abstractmethod
    def set_seats(self, number: int) -> Builder:
        pass
    
    @abstractmethod
    def set_engine(self, engine: str) -> Builder:
        pass

    @abstractmethod
    def set_trip_computer(self) -> Builder:
        pass

    @abstractmethod
    def set_gps(self) -> Builder:
        pass