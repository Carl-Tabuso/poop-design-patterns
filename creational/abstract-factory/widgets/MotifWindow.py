from Window import Window

class MotifWindow(Window):    
    def resize(self) -> str :
        return "Resizing motif window..."

    def render(self) -> str:
        return "Rendering motif window..."
    
    def __str__(self) -> str:
        return "MotifWindow"
