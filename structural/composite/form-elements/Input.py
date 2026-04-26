from FormElement import FormElement

class Input(FormElement):
    def __init__(self, name: str, title: str, type: str) -> None:
        super().__init__(name, title)

        self.__type = type

    def render(self) -> str:
        return "\n".join([
            f"<label for=\"{self._name}\">{self._title}</label>",
            f"<input name=\"{self._name}\" type=\"{self.__type}\" value=\"{self._data}\"/>",
            "" 
        ])