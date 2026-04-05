from Transport import Transport

class Ship(Transport):
    def deliver(self) -> str:
        return "Deliver by sea in a container."