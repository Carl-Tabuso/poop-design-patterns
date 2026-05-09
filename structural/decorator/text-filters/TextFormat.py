from InputFormat import InputFormat
from abc import abstractmethod

class TextFormat(InputFormat):
    def __init__(self, input_format: InputFormat) -> None:
        self._input_format = input_format

    @abstractmethod
    def format_text(self, text: str) -> str:
        return self._input_format.format_text(text)