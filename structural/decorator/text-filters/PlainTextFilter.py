from TextFormat import TextFormat
from re import sub

class PlainTextFilter(TextFormat):
    def format_text(self, text: str) -> str:
        text = super().format_text(text)

        return sub(r"<.*?>", "", text)