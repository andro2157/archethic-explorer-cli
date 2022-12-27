from command.command import Command
from datetime import datetime
import api

class Nodes(Command):
    def __init__(self):
        super().__init__()
    
    def userInput(self, args):
        super().userInput(args)

        for n in api.getNodes():
            print(f"{n['ip']}:{n['port']}")
            print("\tauthorizationDate", Nodes.timestampStrOrNone(n["authorizationDate"]))
            print("\tauthorized", n["authorized"])
            print("\tavailable", n["available"])
            print("\taverageAvailability", n["averageAvailability"])
            print("\tenrollmentDate", Nodes.timestampStrOrNone(n["enrollmentDate"]))
            print("\tfirstPublicKey", n["firstPublicKey"])
            print("\tlastPublicKey", n["lastPublicKey"])
            print("\toriginPublicKey", n["originPublicKey"])
            print("\tgeoPatch", n["geoPatch"])
            print("\tnetworkPatch", n["networkPatch"])
            print("\trewardAddress", n["rewardAddress"])

    def timestampStrOrNone(timestamp):
        if timestamp == None:
            return "None"
        else:
            return str(datetime.fromtimestamp(timestamp))