from Subsystem1 import Subsystem1
from Subsystem2 import Subsystem2
from Facade import Facade
    
if __name__ == "__main__":
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    
    facade = Facade(subsystem1, subsystem2)
    print(facade.operation())