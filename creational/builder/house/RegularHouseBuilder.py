from typing import TYPE_CHECKING
from HouseBuilder import HouseBuilder
from RegularHouse import RegularHouse

if TYPE_CHECKING:
    from Property import Property

class RegularHouseBuilder(HouseBuilder):
    def __init__(self) -> None:
        self.house = RegularHouse()

    def build_walls(self) -> None:
        self.house.walls = 4

    def build_doors(self) -> None:
        self.house.doors = 2

    def build_windows(self) -> None:
        self.house.windows = 4

    def build_roof(self) -> None:
        self.house.roof = True

    def build_garage(self) -> None:
        self.house.garage = True

    def get_result(self) -> Property:
        regular_house = self.house

        self.house = RegularHouse()

        return regular_house