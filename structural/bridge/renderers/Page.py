from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from Renderer import Renderer

class Page(ABC):
    def __init__(self, renderer: Renderer) -> None:
        self._renderer = renderer

    def change_renderer(self, renderer: Renderer) -> None:
        self._renderer = renderer

    @abstractmethod
    def view(self) -> str:
        pass