from State import State

class ConcreteStateA(State):
    def handle1(self) -> None:
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")

        from ConcreteStateB import ConcreteStateB
        self._context.transition_to(ConcreteStateB())

    def handle2(self):
        print("ConcreteStateA handles request2.")
