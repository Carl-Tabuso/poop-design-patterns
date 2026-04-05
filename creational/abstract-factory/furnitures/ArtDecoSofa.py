from Sofa import Sofa

class ArtDecoSofa(Sofa):
    def has_legs(self) -> bool:
        return False
    
    def sit_on(self) -> str:
        return "Sitting on art deco sofa..."
    
    def __str__(self) -> str:
        return "ArtDecoSofa"