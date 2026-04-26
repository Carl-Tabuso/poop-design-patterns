from Renderer import Renderer

class JSONRenderer(Renderer):
    def render_title(self, title: str) -> str:
        return f"\"title\": \"{title}\""
    
    def render_text_block(self, text: str) -> str:
        return f"\"text\": \"{text}\""
    
    def render_image(self, url: str) -> str:
        return f"\"img\": \"{url}\""
    
    def render_link(self, url: str, title: str) -> str:
        return f"\"link\": {{ \"href: \" {url}, \"title: \" {title} }}"
    
    def render_header(self) -> str:
        return ""
    
    def render_footer(self) -> str:
        return ""
    
    def render_parts(self, parts: list) -> str:
        valid_parts = [part for part in parts if part]

        return f"{{\n{",\n".join(valid_parts)} \n}}"