class FrenchLocalizer:
    def __init__(self) -> None:
        self.translations = {
            "car": "voiture",
            "bike": "bicyclette",
            "cycle":"cyclette"
        }

    def translate(self, msg) -> str:
        return self.translations[msg]
