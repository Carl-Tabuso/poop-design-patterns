from FormElement import FormElement

class FieldComposite(FormElement):
    def __init__(self, name: str, title: str) -> None:
        super().__init__(name, title)

        self._fields = {}

    def add(self, field: FormElement) -> None:
        name = field.get_name()
        self._fields[name] = field

    def remove(self, component: FormElement) -> None:
        del self._fields[component]

    def set_data(self, data: dict) -> None:
        for name, field in self._fields.items():
            if name in data:
                field.set_data(data[name])

    def get_data(self) -> dict:
        return self._fields
    
    def render(self) -> str:
        return "".join(field.render() for field in self._fields.values())
