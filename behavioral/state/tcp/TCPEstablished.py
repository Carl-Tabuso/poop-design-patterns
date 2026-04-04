from TCPState import TCPState
from TCPClosed import TCPClosed

class TCPEstablished(TCPState):
    def __init__(self, connection) -> None:
        self.connection = connection

    def close(self) -> None:
        self.connection.set_state(TCPClosed(self.connection))

    def __str__(self) -> str:
        return "TCPEstablished"