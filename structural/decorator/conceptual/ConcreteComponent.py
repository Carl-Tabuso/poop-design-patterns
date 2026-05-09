from Component import Component

class ConcreteComponent(Component):
    def operation(self) -> str:
        return self
    
    def __str__(self) -> str:
        return "ConcreteComponent"