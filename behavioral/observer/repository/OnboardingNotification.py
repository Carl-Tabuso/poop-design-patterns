from Observer import Observer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Repository import Repository

class OnboardingNotification(Observer):
    def __init__(self, email: str) -> None:
        self.__email = email

    def update(self, repository: Repository, event: str = None, data: dict = None) -> None:
        # do email here i guess
        print("OnboardingNotification: The notification has been emailed!")
        