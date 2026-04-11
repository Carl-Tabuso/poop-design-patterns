class Manual:
    def __init__(self) -> None:
        self.seats = 0
        self.engine = None
        self.trip_computer = False
        self.gps = False

    def __str__(self):
        return f"Manual \n\nSeats: {self.seats}\nEngine: {self.engine}\nTrip Computer: {self.trip_computer}\nGPS: {self.gps}"
