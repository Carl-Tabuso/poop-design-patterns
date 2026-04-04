from TCPState import TCPState

class TCPListen(TCPState):
    def __init__(self, connection) -> None:
        self.connection = connection

    def close(self) -> None:
        from TCPClosed import TCPClosed
        self.connection.set_state(TCPClosed(self.connection))

    def acknowledge(self) -> None:
        from TCPEstablished import TCPEstablished
        self.connection.set_state(TCPEstablished(self.connection))

    def __str__(self) -> str:
        return "TCPListen"