from Scrollbar import Scrollbar

class PresentationManagerScrollbar(Scrollbar):
    def scroll(self) -> str:
        return "Presentation manager scrolling..."
    
    def render(self) -> str:
        return "Rendering presentation manager scrollbar..."
    
    def __str__(self) -> str:
        return "PresentationManagerScrollbar"