from abc import ABC, abstractmethod
class Middleware(ABC):
    def __init__(self) -> None:
        self.__next: Middleware|None = None
        
    def link_with(self, next: Middleware) -> Middleware:
        self.__next = next

        return next
    
    @abstractmethod
    def check(self, email: str, password: str) -> bool:
        if self.__next is None:
            return True
        
        return self.__next.check(email, password)