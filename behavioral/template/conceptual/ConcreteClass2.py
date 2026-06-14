from AbstractClass import AbstractClass

class ConcreteClass2(AbstractClass):
    def _required_operations1(self) -> None:
        print("ConcreteClass2 says: Implemented Operation1")

    def _required_operations2(self) -> None:
        print("ConcreteClass2 says: Implemented Operation2")

    def _hook1(self) -> None:
        print("ConcreteClass2 says: Overridden Hook1")
