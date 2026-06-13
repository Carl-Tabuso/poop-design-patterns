from Repository import Repository
from secrets import token_hex
from User import User
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Observer import Observer

class UserRepository(Repository):
    def __init__(self) -> None:
        self.__users: dict[str, User] = {}
        self.__observers: dict[str, list[Observer]] = {"*": []}

    def __init_event_group(self, event: str = "*") -> None:
        if event not in self.__observers:
            self.__observers[event] = []

    def __get_event_observers(self, event: str = "*") -> list[Observer]:
        self.__init_event_group(event)
        group = self.__observers[event]
        x = self.__observers["*"]

        return group + x
    
    def attach(self, observer: Observer, event: str = "*") -> None:
        self.__init_event_group(event)

        self.__observers[event].append(observer)

    def detach(self, observer: Observer, event: str = "*") -> None:
        for _, s in enumerate(self.__get_event_observers(event)):
            if s is observer:
                self.__observers[event].remove(observer)

    def notify(self, event: str = "*", data: str = None) -> None:
        print(f"UserRepository: Broadcasting the {event} event.")
        for observer in self.__get_event_observers(event):
            observer.update(self, event, data)

    def initialize(self, filename: str) -> None:
        print("UserRepository: Loading user records from a file.")

        self.notify("users:init", filename)

    def create_user(self, data: dict) -> User:
        print("UserRepository: Creating a user.")

        user = User()
        user.update(data)

        id = token_hex(16)
        user.update({"id": id})
        self.__users[id] = user

        self.notify("users:created", user.attributes)

        return user
    
    def update_user(self, user: User, data: dict) -> None | User:
        print("UserRepository: Updating a user.")
    
        id = user.attributes["id"]
        if id not in self.__users:
            return None
        
        user = self.__users[id]
        user.update(data)

        self.notify("users:updated", user.attributes)

        return user
    
    def delete_user(self, user: User) -> None:
        print("UserRepository: Deleting a user.")

        id = user.attributes["id"]
        if id not in self.__users:
            return None
        
        self.__users.pop(id, None)

        self.notify("users:deleted", user.attributes)
