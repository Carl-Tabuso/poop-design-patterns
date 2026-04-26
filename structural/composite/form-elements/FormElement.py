from abc import ABC, abstractmethod

class FormElement(ABC):
    def __init__(self, name: str, title: str) -> None:
        self._name = name
        self._title = title
        self._data = None

    def get_name(self) -> str:
        return self._name
    
    def set_data(self, data: dict) -> None:
        self._data = data

    def get_data(self) -> dict:
        return self._data
    
    @abstractmethod
    def render(self) -> str:
        pass