from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from SocialNetworkConnector import SocialNetworkConnector

class SocialNetworkPoster(ABC):
    @abstractmethod
    def get_social_network(self) -> SocialNetworkConnector:
        pass

    def post(self, content: str) -> None:
        social_network = self.get_social_network()

        social_network.log_in()
        social_network.create_post(content)
        social_network.log_out()

    @abstractmethod
    def get_platform_name(self) -> str:
        pass