from AbstractClass import AbstractClass

class ConcreteClass1(AbstractClass):
    def _required_operations1(self) -> None:
        print("ConcreteClass1 says: Implemented Operation1")

    def _required_operations2(self) -> None:
        print("ConcreteClass1 says: Implemented Operation2")
