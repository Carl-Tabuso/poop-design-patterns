from ConcreteComponent import ConcreteComponent
from ConcreteDecoratorA import ConcreteDecoratorA
from ConcreteDecoratorB import ConcreteDecoratorB
    
if __name__ == "__main__":
    component = ConcreteComponent()
    print("Client: I've got a simple component:")
    print(f"RESULT: {component.operation()}")

    print("\n")

    decorator1 = ConcreteDecoratorA(component)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Client: Now I've got a decorated component:")
    print(f"RESULT: {decorator2.operation()}")