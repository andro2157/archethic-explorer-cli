from command.command import Command
import api

class Balance(Command):
    def __init__(self):
        super().__init__()
    
    def userInput(self, args):
        super().userInput(args)

        if len(args) == 0:
            print("balance <address> (exact)")
            print("exact : won't get the last transaction")
        else:
            address = args[0]
            if len(args) < 2 or args[1].lower() != "exact":
                address = api.getLastTransaction(address)
            
            Balance.printBalance(api.getBalance(address))
    
    def printBalance(balance):
        print(f"{balance['uco'] / 1e8} UCO")

        for token in balance["token"]:
            tokenData = api.getToken(token["address"], "symbol, decimals")

            print(f"{token['amount'] / (10 ** int(tokenData['decimals']))} {tokenData['symbol']} ({token['address']})")