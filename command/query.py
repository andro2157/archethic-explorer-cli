from command.command import Command
from connection import con

import json

class Query(Command):
    def __init__(self):
        super().__init__()
    
    def userInput(self, args):
        super().userInput(args)

        if len(args) > 0:
            print(json.dumps(con.executeQuery(" ".join(args)), indent=4))
        else:
            lines = []
            print("Enter the query :")
            
            count = 0

            while True:
                try:
                    line = input("~ ")
                    lines.append(line)
                except KeyboardInterrupt:
                    count = -1000
                    break

                count += line.count("{") - line.count("}")

                if count <= 0:
                    break
            
            if count < 0:
                if count != -1000:
                    print("Invalid query.")
                return
            
            print(json.dumps(con.executeQuery("\n".join(lines)), indent=4))
