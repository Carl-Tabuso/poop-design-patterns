from Builder import Builder
from Car import Car

class CarBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> Builder:
        self.car = Car()

        return self

    def set_seats(self, number: int) -> Builder:
        self.car.seats = number

        return self

    def set_engine(self, engine: str) -> Builder:
        self.car.engine = engine

        return self
    
    def set_trip_computer(self) -> Builder:
        self.car.trip_computer = True

        return self
    
    def set_gps(self) -> Builder:
        self.car.gps = True

        return self
    
    def get_result(self) -> Car:
        car = self.car

        self.reset()

        return car
