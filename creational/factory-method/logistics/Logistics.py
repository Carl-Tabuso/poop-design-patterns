from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from Transport import Transport

class Logistics(ABC):
    def plan_delivery(self) -> str:
        transport = self.create_transport()

        return transport.deliver()

    @abstractmethod
    def create_transport(self) -> Transport:
        pass