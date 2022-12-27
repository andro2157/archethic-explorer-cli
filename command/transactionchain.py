from command.command import Command
from datetime import datetime
import api

class TransactionChain(Command):
    def __init__(self):
        super().__init__()
    
    def userInput(self, args):
        super().userInput(args)

        if len(args) == 0:
            print("chain <address> (pagingaddress)")
            return

        paging = None
        if len(args) >= 2:
            paging = args[1]
        
        for transaction in api.getTransactionChain(args[0], paging):
            print(transaction["address"],
                str(datetime.fromtimestamp(transaction["validationStamp"]["timestamp"])),
                transaction["type"])