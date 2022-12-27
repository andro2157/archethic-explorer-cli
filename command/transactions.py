from command.command import Command
from datetime import datetime
import api

class Transactions(Command):
    def __init__(self):
        super().__init__()
    
    def userInput(self, args):
        super().userInput(args)

        page = None
        if len(args) > 0:
            page = int(args[0])
        
        for transaction in api.getTransactions(page):
            print(transaction["address"],
                str(datetime.fromtimestamp(transaction["validationStamp"]["timestamp"])),
                transaction["type"])