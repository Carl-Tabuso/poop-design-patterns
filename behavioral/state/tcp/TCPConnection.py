from TCPClosed import TCPClosed

class TCPConnection:
    def __init__(self) -> None:
        self.connection = TCPClosed(self)

    def open(self) -> None:
        self.connection.open()

    def close(self) -> None:
        self.connection.close()

    def acknowledge(self) -> None:
        self.connection.acknowledge()
    
    def set_state(self, state) -> None:
        self.connection = state

    def get_state(self):
        return self.connection
    
    def __str__(self) -> str:
        return "TCPConnection"