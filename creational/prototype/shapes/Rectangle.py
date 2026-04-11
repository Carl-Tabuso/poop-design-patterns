from Shape import Shape
import copy

class Rectangle(Shape):
    def __init__(self, width: int | None = None, height: int | None = None) -> None:
        self.width = width
        self.height = height

    def clone(self) -> Shape:
        return copy.deepcopy(self)
    
    def __str__(self) -> str:
        return f"Rectangle(width: {self.width}, height: {self.height})"