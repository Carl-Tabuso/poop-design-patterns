from typing import TYPE_CHECKING
from Logistics import Logistics
from CargoAircraft import CargoAircraft

if TYPE_CHECKING:
    from Transport import Transport

class AirLogistics(Logistics):
    def create_transport(self) -> Transport:
        return CargoAircraft()