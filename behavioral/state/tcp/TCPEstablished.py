from typing import TYPE_CHECKING

from TCPState import TCPState
from TCPClosed import TCPClosed

if TYPE_CHECKING:
    from TCPConnection import TCPConnection

class TCPEstablished(TCPState):
    def __init__(self, connection: TCPConnection) -> None:
        self.connection = connection

    def close(self) -> None:
        self.connection.set_state(TCPClosed(self.connection))

    def __str__(self) -> str:
        return "TCPEstablished"