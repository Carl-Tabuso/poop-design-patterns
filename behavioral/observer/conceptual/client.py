from ConcreteSubject import ConcreteSubject
from ConcreteObserverA import ConcreteObserverA
from ConcreteObserverB import ConcreteObserverB

if __name__ == "__main__":
    subject = ConcreteSubject()

    observer1 = ConcreteObserverA()
    subject.attach(observer1)

    observer2 = ConcreteObserverB()
    subject.attach(observer2)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer2)

    subject.some_business_logic()
