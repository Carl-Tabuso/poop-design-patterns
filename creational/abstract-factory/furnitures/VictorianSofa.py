from Sofa import Sofa

class VictorianSofa(Sofa):
    def has_legs(self) -> bool:
        return True
    
    def sit_on(self) -> str:
        return f"Sitting on {self}..."
    
    def __str__(self) -> str:
        return "VictorianSofa"