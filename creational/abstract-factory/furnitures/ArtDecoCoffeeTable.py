from CoffeeTable import CoffeeTable

class ArtDecoCoffeeTable(CoffeeTable):
    def has_legs(self) -> bool:
        return False
    
    def sit_on(self) -> str:
        return "Sitting on art deco coffee table..."
    
    def __str__(self) -> str:
        return "ArtDecoCoffeeTable"