from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Subsystem1 import Subsystem1
    from Subsystem2 import Subsystem2

class Facade:
    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        self._subsystem1 = subsystem1
        self._subsystem2 = subsystem2

    def operation(self) -> str:
        result = "Facade initializes subsystems:\n"
        result += self._subsystem1.operation1()
        result += self._subsystem2.operation1()
        result += "Facade orders subsystems to perform the action:\n"
        result += self._subsystem1.operationN()
        result += self._subsystem2.operationZ()

        return result