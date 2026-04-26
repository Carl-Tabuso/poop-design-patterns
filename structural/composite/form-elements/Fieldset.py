from FieldComposite import FieldComposite

class Fieldset(FieldComposite):
    def render(self) -> str:
        output = super().render()

        return "\n".join([
            f"<fieldset><legend>{self._title}</legend>",
            f"{output}</fieldset>",
            ""
        ]) 