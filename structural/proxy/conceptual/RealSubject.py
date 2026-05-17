from Subject import Subject

class RealSubject(Subject):
    def request(self) -> None:
        print(f"{self}: Handling request.")
    
    def __str__(self) -> str:
        return "RealSubject"