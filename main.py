from command.help import Help
from command.query import Query
from command.last import Last
from command.balance import Balance
from command.token import Token
from command.endpoint import Endpoint
from command.oracle import Oracle
from command.transactions import Transactions
from command.transaction import Transaction
from command.nodes import Nodes
from command.transactionchain import TransactionChain
from command.networktransactions import NetworkTransactions

from connection import con

import traceback

VERSION = "1.1"

commands = {
    "help": Help(),
    "query": Query(),
    "last": Last(),
    "balance": Balance(),
    "token": Token(),
    "endpoint": Endpoint(),
    "oracle": Oracle(),
    "transactions": Transactions(),
    "transaction": Transaction(),
    "nodes": Nodes(),
    "chain": TransactionChain(),
    "type": NetworkTransactions()
}

if __name__ == "__main__":
    print(f"Archethic Explorer CLI {VERSION}")
    print(f"https://github.com/andro2157/archethic-explorer-cli/")
    print(f"Endpoint : {con.endpoint}")

    while True:
        try:
            command = input("> ")
        except KeyboardInterrupt:
            break

        args = command.split()

        if len(args) == 0: continue

        if args[0].lower() in commands:
            try:
                commands[args[0].lower()].userInput(args[1:])
            except Exception as e:
                print("Command failed.")
                print(traceback.format_exc())
        else:
            print("Unknown command.")