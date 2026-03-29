class SpanishLocalizer:
    def __init__(self) -> None:
        self.translations = {
            "car": "coche", 
            "bike": "bicicleta",
            "cycle":"ciclo"
        }

    def translate(self, msg: str) -> str:
        return self.translations[msg]
