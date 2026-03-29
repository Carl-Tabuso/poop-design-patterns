from Scrollbar import Scrollbar

class MotifScrollbar(Scrollbar):
    def scroll(self) -> str:
        return "Motif scrolling..."
    
    def render(self) -> str:
        return "Rendering motif scrollbar..."
    
    def __str__(self) -> str:
        return "MotifScrollbar"
