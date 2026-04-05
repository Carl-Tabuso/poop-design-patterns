from typing import TYPE_CHECKING
from SocialNetworkPoster import SocialNetworkPoster
from LinkedInConnector import LinkedInConnector

if TYPE_CHECKING:
    from SocialNetworkConnector import SocialNetworkConnector

class LinkedInPoster(SocialNetworkPoster):
    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = password

    def get_social_network(self) -> SocialNetworkConnector:
        return LinkedInConnector(self.email, self.password)
    
    def get_platform_name(self) -> str:
        return "Facebook"    