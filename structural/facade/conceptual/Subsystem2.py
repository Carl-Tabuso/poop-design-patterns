class Subsystem2:
    def operation1(self) -> str:
        return f"{self}: Get ready!\n"
    
    def operationZ(self) -> str:
        return f"{self}: Fire!\n"

    def __str__(self) -> str:
        return "Subsystem2"