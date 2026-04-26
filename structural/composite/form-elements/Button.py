from FormElement import FormElement

class Button(FormElement):
    def __init__(self, name: str, title: str, type: str) -> None:
        super().__init__(name, title)

        self.__type = type

    def render(self) -> str:
        return f"<button name=\"{self._name}\" type=\"{self.__type}\">{self._title}</button>"
