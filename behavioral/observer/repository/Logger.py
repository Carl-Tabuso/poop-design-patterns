from Observer import Observer
from pathlib import Path
from datetime import datetime
from typing import TYPE_CHECKING
import json
import os

if TYPE_CHECKING:
    from Repository import Repository

class Logger(Observer):
    def __init__(self, filename) -> None:
        self.__filename = filename

        if Path(self.__filename).exists():
            os.remove(self.__filename)

    def update(self, repository: Repository, event: str = None, data: dict = None) -> None:
        entry = f"{datetime.now():%Y-%m-%d %H:%M:%S}: '{event}' with data '{json.dumps(data)}'\n"

        with open(self.__filename, "a", encoding="utf-8") as f:
            f.write(entry)

        print(f"Logger: I've written '{event}' entry to the log.")