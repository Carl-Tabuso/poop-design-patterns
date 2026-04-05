from typing import TYPE_CHECKING
from Logistics import Logistics
from Truck import Truck

if TYPE_CHECKING:
    from Transport import Transport

class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()