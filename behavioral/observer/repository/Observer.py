from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Repository import Repository

class Observer(ABC):
    @abstractmethod
    def update(self, repository: Repository, event: str, data: str) -> None:
        pass