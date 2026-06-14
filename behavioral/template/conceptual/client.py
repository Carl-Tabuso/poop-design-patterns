from ConcreteClass1 import ConcreteClass1
from ConcreteClass2 import ConcreteClass2

if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    cls1 = ConcreteClass1()
    cls1.template_method()

    print("\n")

    print("Same client code can work with different subclasses:")
    cls2 = ConcreteClass2()
    cls2.template_method()
