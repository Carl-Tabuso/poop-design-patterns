from typing import TYPE_CHECKING
from Page import Page

if TYPE_CHECKING:
    from Renderer import Renderer

class SimplePage(Page):
    def __init__(self, renderer: Renderer, title: str, content: str) -> None:
        super().__init__(renderer)
        
        self._title = title
        self._content = content

    def view(self) -> str:
        return self._renderer.render_parts([
            self._renderer.render_header(),
            self._renderer.render_title(self._title),
            self._renderer.render_text_block(self._content),
            self._renderer.render_footer(),
        ])