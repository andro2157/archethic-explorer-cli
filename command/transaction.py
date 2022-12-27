from command.command import Command
from datetime import datetime
import api
import json

class Transaction(Command):
    def __init__(self):
        super().__init__()
    
    def userInput(self, args):
        super().userInput(args)

        if len(args) == 0:
            print("transaction <address> (raw)")
        else:
            if len(args) >= 2 and args[1].lower() == "raw":
                print(json.dumps(api.getTransaction(args[0]), indent=4))
                return

            t = api.getTransaction(args[0])

            print(f"Type : {t['type']}")
            print(f"Timestamp : {str(datetime.fromtimestamp(t['validationStamp']['timestamp']))}")
            print(f"Chain Length : {t['chainLength']}")
            print(f"Version : {t['version']}")

            if t["type"] == "transfer":
                print(f"Fee : {t['validationStamp']['ledgerOperations']['fee'] / 1e8} UCO")
                print("\nInputs : ")
                for i in t["inputs"]:
                    outstr = "SPENT " if i["spent"] else ""
                    outstr += str(datetime.fromtimestamp(i["timestamp"])) + " "

                    if i["type"] == "UCO":
                        outstr += f"{i['amount'] / 1e8} UCO from {i['from']}"
                    elif i["type"] == "token":
                        tokenData = api.getToken(i["tokenAddress"], "symbol, decimals")
                        outstr += f"{i['amount'] / (10 ** int(tokenData['decimals']))} {tokenData['symbol']} (id {i['tokenId']}, {i['tokenAddress']}) from {i['from']}"
                    else:
                        outstr += f"{i['amount']} from {i['from']}"
                    
                    print("\t" + outstr)

                print("\nMovements :")
                for i in t["validationStamp"]["ledgerOperations"]["transactionMovements"]:
                    if i["type"] == "UCO":
                        outstr = f"{i['amount'] / 1e8} UCO to {i['to']}"
                    elif i["type"] == "token":
                        tokenData = api.getToken(i["tokenAddress"], "symbol, decimals")
                        outstr = f"{i['amount'] / (10 ** int(tokenData['decimals']))} {tokenData['symbol']} (id {i['tokenId']}, {i['tokenAddress']}) to {i['to']}"
                    else:
                        outstr = f"{i['amount']} to {i['to']}"
                    
                    print("\t" + outstr)
                
                print("\nUnspent outputs :")
                for i in t["validationStamp"]["ledgerOperations"]["unspentOutputs"]:
                    if i["type"] == "UCO":
                        outstr = f"{i['amount'] / 1e8} UCO from {i['from']}"
                    elif i["type"] == "token":
                        tokenData = api.getToken(i["tokenAddress"], "symbol, decimals")
                        outstr = f"{i['amount'] / (10 ** int(tokenData['decimals']))} {tokenData['symbol']} (id {i['tokenId']}, {i['tokenAddress']}) from {i['from']}"
                    else:
                        outstr = f"{i['amount']} from {i['from']}"
                    
                    print("\t" + outstr)
            elif t["type"] == "keychain":
                print("Authentifications :")
                for auth in json.loads(t["data"]["content"])["authentication"]:
                    print(auth)