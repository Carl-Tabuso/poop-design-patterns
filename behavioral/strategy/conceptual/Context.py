from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Strategy import Strategy

class Context:
    __strategy: Strategy | None = None

    def __init__(self, strategy: Strategy) -> None:
        self.__strategy = strategy

    def set_strategy(self, strategy: Strategy) -> None:
        self.__strategy = strategy

    def do_some_business_logic(self) -> None:
        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self.__strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(f"{",".join(result)}")
