from typing import TYPE_CHECKING
from TCPState import TCPState

if TYPE_CHECKING:
    from TCPConnection import TCPConnection

class TCPListen(TCPState):
    def __init__(self, connection: TCPConnection) -> None:
        self.connection = connection

    def close(self) -> None:
        from TCPClosed import TCPClosed
        self.connection.set_state(TCPClosed(self.connection))

    def acknowledge(self) -> None:
        from TCPEstablished import TCPEstablished
        self.connection.set_state(TCPEstablished(self.connection))

    def __str__(self) -> str:
        return "TCPListen"