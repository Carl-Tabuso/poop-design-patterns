from typing import TYPE_CHECKING
from WidgetFactory import WidgetFactory
from MotifScrollbar import MotifScrollbar
from MotifWindow import MotifWindow

if TYPE_CHECKING:
    from Scrollbar import Scrollbar
    from Window import Window

class MotifWidgetFactory(WidgetFactory):
    def create_scrollbar(self) -> Scrollbar:
        return MotifScrollbar()
    
    def create_window(self) -> Window:
        return MotifWindow()

    def __str__(self) -> str:
        return "MotifWidgetFactory"
