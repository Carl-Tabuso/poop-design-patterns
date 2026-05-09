from InputFormat import InputFormat

class TextInput(InputFormat):
    def format_text(self, text: str) -> str:
        return text