from Chair import Chair

class ArtDecoChair(Chair):
    def has_legs(self) -> bool:
        return False
    
    def sit_on(self) -> str:
        return "Sitting on art deco chair..."
    
    def __str__(self) -> str:
        return "ArtDecoChair"