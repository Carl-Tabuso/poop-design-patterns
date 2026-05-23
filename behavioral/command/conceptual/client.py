from Invoker import Invoker
from SimpleCommand import SimpleCommand
from Receiver import Receiver
from ComplexCommand import ComplexCommand
        
if __name__ == "__main__":
    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Say Hi!"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(receiver, "Send Email", "Save Report"))

    invoker.do_something_important()