from command.command import Command
import api
import base64
import re

class Token(Command):
    def __init__(self):
        super().__init__()
    
    def userInput(self, args):
        super().userInput(args)

        if len(args) == 0:
            print("token <address> (dump)")
            print("dump : dumps the raw content")
        else:
            if len(args) >= 2 and args[1].lower() == "dump":
                tokenData = api.getToken(args[0])
                if "properties" in tokenData and "content" in tokenData["properties"] \
                    and "raw" in tokenData["properties"]["content"]:
                    if "type_mime" in tokenData["properties"]:
                        print(f"Type : {tokenData['properties']['type_mime']}")
                        ext = tokenData["properties"]["type_mime"].split("/")[1]
                    else:
                        print("Unknown type")
                        ext = "data"
                    
                    filename = re.sub(r'[^\w\d-]','_', tokenData["name"])[:20] + "_" + args[0] + "." + ext
                    
                    newname = input(f"Filename ? > (Default : {filename})")
                    if newname != "":
                        filename = newname

                    with open(filename, "wb") as f:
                        f.write(base64.b64decode(tokenData["properties"]["content"]["raw"].encode("ascii")))
                    
                    print(f"Saved to {filename}")
            else:
                Token.printToken(api.getToken(args[0]))
    
    def printToken(tokenData):
        print(f"{tokenData['name']} (${tokenData['symbol']}) id : {tokenData['id']}")
        print(f"Supply : {tokenData['supply']} (Decimals : {tokenData['decimals']})")
        print(f"Type : {tokenData['type']}")
        print(f"Genesis : {tokenData['genesis']}")

        print("Proprties :")
        for p in tokenData["properties"]:
            data = str(tokenData["properties"][p])
            if len(data) > 50:
                data = data[:50] + "..."
            
            print(f"\t{p} : {data}")