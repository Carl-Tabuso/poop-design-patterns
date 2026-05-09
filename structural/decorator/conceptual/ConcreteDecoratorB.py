from Decorator import Decorator

class ConcreteDecoratorB(Decorator):
    def operation(self):
        return f"{self}({super().operation()})"
    
    def __str__(self) -> str:
        return "ConcreteDecoratorB"