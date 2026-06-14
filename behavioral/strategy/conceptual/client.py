from Context import Context
from ConcreteStrategyA import ConcreteStrategyA
from ConcreteStrategyB import ConcreteStrategyB

if __name__ == "__main__":
    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()

    print("\n")

    print("Client: Strategy is set to reverse sorting.")
    context.set_strategy(ConcreteStrategyB())
    context.do_some_business_logic()
