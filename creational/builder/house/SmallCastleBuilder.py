from typing import TYPE_CHECKING
from HouseBuilder import HouseBuilder
from SmallCastle import SmallCastle

if TYPE_CHECKING:
    from Property import Property

class SmallCastleBuilder(HouseBuilder):
    def __init__(self):
        self.castle = SmallCastle()

    def build_walls(self) -> None:
        self.castle.walls = 8

    def build_doors(self) -> None:
        self.castle.doors = 4

    def build_windows(self) -> None:
        self.castle.windows = 8

    def build_roof(self) -> None:
        self.castle.roof = True

    def build_garage(self) -> None:
        self.castle.garage = True

    def get_result(self) -> Property:
        small_castle = self.castle

        self.castle = SmallCastle()

        return small_castle
