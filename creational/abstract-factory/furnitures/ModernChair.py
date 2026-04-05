from Chair import Chair

class ModernChair(Chair):
    def has_legs(self) -> bool:
        return False

    def sit_on(self) -> str:
        return f"Sitting on {self}..."
    
    def __str__(self) -> str:
        return "ModernChair"