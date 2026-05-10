class Subsystem1:
    def operation1(self) -> str:
        return f"{self}: Ready!\n"
    
    def operationN(self) -> str:
        return f"{self}: Go!\n"

    def __str__(self) -> str:
        return "Subsystem1"