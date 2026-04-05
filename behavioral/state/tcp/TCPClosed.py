from typing import TYPE_CHECKING
from TCPState import TCPState

if TYPE_CHECKING:
    from TCPConnection import TCPConnection

class TCPClosed(TCPState):
    def __init__(self, connection: TCPConnection) -> None:
        self.connection = connection

    def open(self) -> None:
        from TCPListen import TCPListen
        self.connection.set_state(TCPListen(self.connection))

    def __str__(self) -> str:
        return "TCPClosed"