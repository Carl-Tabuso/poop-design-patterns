from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self) -> None:
        self._base_operation1()
        self._required_operations1()
        self._base_operation2()
        self._hook1()
        self._required_operations2()
        self._base_operation3()
        self._hook2()

    def _base_operation1(self) -> None:
        print("AbstractClass says: I am doing the bulk of the work")

    def _base_operation2(self) -> None:
        print("AbstractClass says: But I let subclasses override some operations")

    def _base_operation3(self) -> None:
        print("AbstractClass says: But I am doing the bulk of the work anyway")

    @abstractmethod
    def _required_operations1(self) -> None:
        pass

    @abstractmethod
    def _required_operations2(self) -> None:
        pass

    def _hook1(self) -> None:
        pass

    def _hook2(self) -> None:
        pass
    