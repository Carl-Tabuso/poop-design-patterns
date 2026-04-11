from Builder import Builder
from Manual import Manual

class CarManualBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> Builder:
        self.manual = Manual()

        return self

    def set_seats(self, number: int) -> Builder:
        self.manual.seats = number

        return self

    def set_engine(self, engine: str) -> Builder:
        self.manual.engine = engine

        return self
    
    def set_trip_computer(self) -> Builder:
        self.manual.trip_computer = True

        return self
    
    def set_gps(self) -> Builder:
        self.manual.gps = True

        return self
    
    def get_result(self) -> Manual:
        manual = self.manual

        self.reset()

        return manual
