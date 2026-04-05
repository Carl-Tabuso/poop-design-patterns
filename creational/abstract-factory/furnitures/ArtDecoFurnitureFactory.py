from typing import TYPE_CHECKING
from FurnitureFactory import FurnitureFactory
from ArtDecoChair import ArtDecoChair
from ArtDecoSofa import ArtDecoSofa
from ArtDecoCoffeeTable import ArtDecoCoffeeTable

if TYPE_CHECKING:
    from Chair import Chair
    from Sofa import Sofa
    from CoffeeTable import CoffeeTable

class ArtDecoFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ArtDecoChair()

    def create_sofa(self) -> Sofa:
        return ArtDecoSofa()

    def create_coffee_table(self) -> CoffeeTable:
        return ArtDecoCoffeeTable()