from TCPStateContract import TCPStateContract

class TCPState(TCPStateContract):
    def open(self) -> None:
        raise Exception("Invalid state transition.")

    def close(self) -> None:
        raise Exception("Invalid state transition.")

    def acknowledge(self) -> None:
        raise Exception("Invalid state transition.")
    
    def __str__(self) -> str:
        return "TCPState"