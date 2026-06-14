from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from State import State

class Context:
    __state: State | None = None

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State) -> None:
        print(f"Context: Transition to {state.__class__.__name__}.")
        self.__state = state
        self.__state.set_context(self)

    def request1(self) -> None:
        self.__state.handle1()

    def request2(self) -> None:
        self.__state.handle2()
