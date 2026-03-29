from WidgetFactory import WidgetFactory
from MotifScrollbar import MotifScrollbar
from MotifWindow import MotifWindow

class MotifWidgetFactory(WidgetFactory):
    @staticmethod
    def create_scrollbar() -> MotifScrollbar:
        return MotifScrollbar()
    
    @staticmethod
    def create_window() -> MotifWindow:
        return MotifWindow()
    
    def __str__(self) -> str:
        return "MotifWidgetFactory"
