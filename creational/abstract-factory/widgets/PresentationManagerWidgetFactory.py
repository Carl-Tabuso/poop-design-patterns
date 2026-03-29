from WidgetFactory import WidgetFactory
from PresentationManagerScrollbar import PresentationManagerScrollbar
from PresentationManagerWindow import PresentationManagerWindow

class PresentationManagerWidgetFactory(WidgetFactory):
    @staticmethod
    def create_scrollbar() -> PresentationManagerScrollbar:
        return PresentationManagerScrollbar()

    @staticmethod
    def create_window() -> PresentationManagerWindow:
        return PresentationManagerWindow()
    
    def __str__(self) -> str:
        return "PresentationManagerWidgetFactory"