from Circle import Circle
from Rectangle import Rectangle

def display_shapes(shapes: list) -> None:
    for shape in shapes:
        print(shape)

if __name__ == '__main__':
    shapes = []

    circle = Circle()
    circle.radius = 20
    shapes.append(circle)

    circle_clone = circle.clone()
    shapes.append(circle_clone)

    rectangle = Rectangle()
    rectangle.width = 10
    rectangle.height = 20
    shapes.append(rectangle)

    rectangle_clone = rectangle.clone()
    shapes.append(rectangle_clone)

    display_shapes(shapes)