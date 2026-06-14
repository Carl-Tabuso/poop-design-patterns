from Context import Context
from ConcreteStateA import ConcreteStateA

if __name__ == "__main__":
    context = Context(ConcreteStateA())
    context.request1()
    context.request2()
