from Component import Component
from abc import abstractmethod

class Decorator(Component):
    def __init__(self, component: Component) -> None:
        self._component = component

    @abstractmethod
    def operation(self) -> str:
        return self._component.operation()