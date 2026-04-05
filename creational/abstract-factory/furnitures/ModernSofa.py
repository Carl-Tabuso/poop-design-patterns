from Sofa import Sofa

class ModernSofa(Sofa):
    def has_legs(self) -> bool:
        return False
    
    def sit_on(self) -> str:
        return f"Sitting on {self}..."
    
    def __str__(self) -> str:
        return "ModernSofa"