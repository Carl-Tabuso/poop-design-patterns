from typing import TYPE_CHECKING
from MonkeyHandler import MonkeyHandler
from SquirrelHandler import SquirrelHandler
from DogHandler import DogHandler

if TYPE_CHECKING:
    from Handler import Handler

def client_code(handler: Handler) -> None:
    foods = ["Nut", "Banana", "Cup of coffee"]

    for food in foods:
        print(f"Client: Who wants a {food}?")
        result = handler.handle(food)
        if result:
            print(f"  {result}")
        else:
            print(f"  {food} was left untouched.")

if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    print("Chain: Monkey > Squirrel > Dog\n")
    client_code(monkey)
    print("\n")

    print("Subchain: Squirrel > Dog\n")
    client_code(squirrel)