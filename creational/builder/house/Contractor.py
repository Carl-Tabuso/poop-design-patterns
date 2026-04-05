from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from HouseBuilder import HouseBuilder
    from Property import Property

class Contractor:
    def __init__(self) -> None:
        self.builder: HouseBuilder | None = None

    def set_builder(self, builder: HouseBuilder) -> None:
        self.builder = builder

    def make_regular_house(self) -> Property:
        self.builder.build_walls()
        self.builder.build_doors()
        self.builder.build_windows()
        self.builder.build_roof()

        return self.builder.get_result()

    def make_small_castle(self) -> Property:
        self.builder.build_walls()
        self.builder.build_doors()
        self.builder.build_windows()
        self.builder.build_roof()
        self.builder.build_garage()

        return self.builder.get_result()    