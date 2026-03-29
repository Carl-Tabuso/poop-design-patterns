from Window import Window

class PresentationManagerWindow(Window):
    def resize(self) -> str:
        return "Resizing presentation manager window..."

    def render(self) -> str:
        return "Rendering presentation manager window..."
    
    def __str__(self) -> str:
        return "PresentationManagerWindow"
