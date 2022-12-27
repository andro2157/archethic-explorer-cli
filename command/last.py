from command.command import Command
import api

class Last(Command):
    def __init__(self):
        super().__init__()
    
    def userInput(self, args):
        super().userInput(args)

        if len(args) == 0:
            print("last <address>")
        else:
            print(api.getLastTransaction(args[0]))