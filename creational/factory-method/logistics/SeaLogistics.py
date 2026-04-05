from typing import TYPE_CHECKING
from Logistics import Logistics
from Ship import Ship

if TYPE_CHECKING:
    from Transport import Transport

class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()