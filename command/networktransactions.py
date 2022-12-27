from command.command import Command
from datetime import datetime
import api

class NetworkTransactions(Command):
    def __init__(self):
        super().__init__()
    
    def userInput(self, args):
        super().userInput(args)

        if len(args) == 0:
            print("type <type> (page)")
            return

        page = None
        if len(args) >= 2:
            page = int(args[1])
        
        for transaction in api.getNetworkTransactions(args[0], page):
            print(transaction["address"],
                str(datetime.fromtimestamp(transaction["validationStamp"]["timestamp"])),
                transaction["type"])