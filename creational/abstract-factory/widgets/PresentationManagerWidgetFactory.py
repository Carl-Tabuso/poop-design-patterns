from typing import TYPE_CHECKING
from WidgetFactory import WidgetFactory
from PresentationManagerScrollbar import PresentationManagerScrollbar
from PresentationManagerWindow import PresentationManagerWindow

if TYPE_CHECKING:
    from Scrollbar import Scrollbar
    from Window import Window

class PresentationManagerWidgetFactory(WidgetFactory):
    def create_scrollbar(self) -> Scrollbar:
        return PresentationManagerScrollbar()

    def create_window(self) -> Window:
        return PresentationManagerWindow()
    
    def __str__(self) -> str:
        return "PresentationManagerWidgetFactory"