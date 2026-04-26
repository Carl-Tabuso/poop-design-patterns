from Renderer import Renderer

class HTMLRenderer(Renderer):
    def render_title(self, title: str) -> str:
        return f"<h1>{title}</h1>"
    
    def render_text_block(self, text: str) -> str:
        return f"<div class=\"text\">{text}</div>"
    
    def render_image(self, url: str) -> str:
        return f"<img src=\"{url}\" />"
    
    def render_link(self, url: str, title: str) -> str:
        return f"<a href=\"{url}\">{title}</a>"
    
    def render_header(self) -> str:
        return "<html><body>"
    
    def render_footer(self) -> str:
        return "</body></html>"
    
    def render_parts(self, parts: list) -> str:
        return "\n".join(parts)