from typing import TYPE_CHECKING

from FurnitureFactory import FurnitureFactory
from VictorianChair import VictorianChair
from VictorianSofa import VictorianSofa
from VictorianCoffeeTable import VictorianCoffeeTable

if TYPE_CHECKING:
    from Chair import Chair
    from Sofa import Sofa
    from CoffeeTable import CoffeeTable

class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_sofa(self) -> Sofa:
        return VictorianSofa()

    def create_coffee_table(self) -> CoffeeTable:
        return VictorianCoffeeTable()