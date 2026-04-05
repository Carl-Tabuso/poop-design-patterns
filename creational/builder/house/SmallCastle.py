from Property import Property

class SmallCastle(Property):
    def __init__(self):
        self.walls: int = 0
        self.doors: int = 0
        self.windows: int = 0
        self.roof: bool = False
        self.garage: bool = False

    def __str__(self) -> str:
        return f"SmallCastle:\nWalls: {self.walls}\nDoors: {self.doors}\nWindows: {self.windows}\nHasRoof: {self.roof}\nHasGarage: {self.garage}"