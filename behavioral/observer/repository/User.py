class User:
    attributes: dict[str, str] = {}

    def update(self, data: dict[str, str]) -> None:
        self.attributes = self.attributes | data
