from FurnitureFactory import FurnitureFactory
from ModernChair import ModernChair
from ModernSofa import ModernSofa
from ModernCoffeeTable import ModernCoffeeTable
from Chair import Chair
from Sofa import Sofa
from CoffeeTable import CoffeeTable

class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_sofa(self) -> Sofa:
        return ModernSofa()

    def create_coffee_table(self) -> CoffeeTable:
        return ModernCoffeeTable()