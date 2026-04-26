from typing import TYPE_CHECKING
from Page import Page

if TYPE_CHECKING:
    from Renderer import Renderer
    from Product import Product

class ProductPage(Page):
    def __init__(self, renderer: Renderer, product: Product) -> None:
        super().__init__(renderer)
        
        self._product = product

    def view(self) -> str:
        return self._renderer.render_parts([
            self._renderer.render_header(),
            self._renderer.render_title(self._product.get_title()),
            self._renderer.render_text_block(self._product.get_description()),
            self._renderer.render_image(self._product.get_image()),
            self._renderer.render_text_block(f"${self._product.get_price():,.2f}"),
            self._renderer.render_link(f"/cart/add/{self._product.get_id()}", "Add to cart"),
            self._renderer.render_footer(),
        ])