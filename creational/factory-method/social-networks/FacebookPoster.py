from typing import TYPE_CHECKING
from SocialNetworkPoster import SocialNetworkPoster
from FacebookConnector import FacebookConnector

if TYPE_CHECKING:
    from SocialNetworkConnector import SocialNetworkConnector

class FacebookPoster(SocialNetworkPoster):
    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = password

    def get_social_network(self) -> SocialNetworkConnector:
        return FacebookConnector(self.email, self.password)
    
    def get_platform_name(self) -> str:
        return "Facebook"