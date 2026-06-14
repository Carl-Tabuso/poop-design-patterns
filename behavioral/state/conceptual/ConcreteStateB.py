from State import State

class ConcreteStateB(State):
    def handle1(self) -> None:
        print("ConcreteStateB handles request1.")

    def handle2(self) -> None:
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")

        from ConcreteStateA import ConcreteStateA
        self._context.transition_to(ConcreteStateA())
