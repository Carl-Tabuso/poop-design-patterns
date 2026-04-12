import time

class Database:
    _instance: Database | None = None

    def __new__(cls) -> Database:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._connection = None

        return cls._instance

    def get_connection(self) -> str:
        return self._connection

    def set_connection(self, connection: str) -> str:
        self._connection = connection

        return self._connection

    def query(self, stmt: str) -> None:
        print(f"Executing: {stmt}")

        time.sleep(1)

        return "Query executed."