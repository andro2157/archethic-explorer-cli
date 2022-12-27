from command.command import Command
from connection import con, ARCHETHIC_MAINNET, ARCHETHIC_TESTNET
import api

class Endpoint(Command):
    def __init__(self):
        super().__init__()
    
    def userInput(self, args):
        super().userInput(args)

        if len(args) == 0:
            print(f"Endpoint : {con.endpoint}")
        else:
            if args[0] == "mainnet":
                con.endpoint = ARCHETHIC_MAINNET
            elif args[0] == "testnet":
                con.endpoint = ARCHETHIC_TESTNET
            elif args[0] == "nearest":
                endpoints = Endpoint.getNearestEndpointsList()
                if len(endpoints) == 0:
                    print("No available endpoints")
                    return
                
                con.endpoint = endpoints[0]
            elif args[0] == "list":
                for endpoint in Endpoint.getNearestEndpointsList():
                    print(endpoint)
                return
            elif args[0] == "custom":
                if len(args) >= 2:
                    con.endpoint = args[1]
                else:
                    con.endpoint = input("Custom endpoint >")
                if not con.endpoint.startswith("http"):
                    print("Warning : the endpoint should start with the protocol (http:// or https://)")

            print(f"Endpoint : {con.endpoint}")
    
    def getNearestEndpointsList():
        return list(map(lambda x: f"http://{x['ip']}:{x['port']}", api.getNearestEndpoints()))
        