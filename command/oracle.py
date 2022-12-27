from command.command import Command
import api

class Oracle(Command):
    def __init__(self):
        super().__init__()
    
    def userInput(self, args):
        super().userInput(args)

        timestamp = None
        if len(args) > 0:
            timestamp = int(args[0])
        
        oracleData = api.getOracleData(timestamp)

        print(f"Timestamp : {oracleData['timestamp']}")
        print(f"Price :\n${oracleData['services']['uco']['usd']}\n{oracleData['services']['uco']['eur']}€")