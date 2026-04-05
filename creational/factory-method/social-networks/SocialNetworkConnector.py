from abc import ABC, abstractmethod

class SocialNetworkConnector(ABC):
    @abstractmethod
    def log_in(self) -> None:
        pass

    @abstractmethod
    def log_out(self) -> None:
        pass

    @abstractmethod
    def create_post(self, content: str) -> None:
        pass

    @abstractmethod
    def name(self) -> str:
        pass