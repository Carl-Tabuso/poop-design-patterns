from Strategy import Strategy

class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: list) -> list:
        return sorted(data, reverse=True)
    