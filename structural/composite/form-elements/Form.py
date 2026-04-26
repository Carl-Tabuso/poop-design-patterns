from FieldComposite import FieldComposite

class Form(FieldComposite):
    def __init__(self, name: str, title: str, url: str) -> None:
        super().__init__(name, title)

        self.__url = url

    def render(self) -> str:
        output = super().render()

        return "\n".join([
            f"<form action=\"{self.__url}\">",
            f"<h3>{self._title}</h3>",
            f"{output}",
            "</form>"
        ])