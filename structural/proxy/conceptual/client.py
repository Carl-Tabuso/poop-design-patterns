from RealSubject import RealSubject
from Proxy import Proxy

if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    real_subject.request()

    print("\n")

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    proxy.request()