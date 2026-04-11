from Shape import Shape
import copy

class Circle(Shape):
    def __init__(self, radius: int | None = None):
        self.radius = radius

    def clone(self) -> Shape:
        return copy.deepcopy(self)

    def __str__(self) -> str:
        return f"Circle(radius: {self.radius})"