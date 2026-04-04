from TCPState import TCPState
from TCPListen import TCPListen

class TCPClosed(TCPState):
    def __init__(self, connection) -> None:
        self.connection = connection

    def open(self) -> None:
        self.connection.set_state(TCPListen(self.connection))

    def __str__(self) -> str:
        return "TCPClosed"