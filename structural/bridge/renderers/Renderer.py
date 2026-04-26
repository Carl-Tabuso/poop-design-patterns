from abc import ABC, abstractmethod

class Renderer(ABC):
    @abstractmethod
    def render_title(self, title: str) -> str:
        pass

    @abstractmethod
    def render_text_block(self, text: str) -> str:
        pass

    @abstractmethod
    def render_image(self, url: str) -> str:
        pass

    @abstractmethod
    def render_link(self, url: str, title: str) -> str:
        pass

    @abstractmethod
    def render_header(self) -> str:
        pass

    @abstractmethod
    def render_footer(self) -> str:
        pass

    @abstractmethod
    def render_parts(self, parts: list) -> str:
        pass