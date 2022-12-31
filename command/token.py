from command.command import Command
import api
import base64
import re
import json
import requests
import os

class Token(Command):
    def __init__(self):
        super().__init__()
    
    def userInput(self, args):
        super().userInput(args)

        if len(args) == 0:
            print("token <address> (dump, full)")
            print("dump : dumps the raw content / the collection")
            print("full : lists all elements of the collection")
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
                        f.write(Token.dumpContent(tokenData["properties"]["content"]))
                    
                    print(f"Saved to {filename}")
                if "collection" in tokenData and len(tokenData["collection"]) > 0:
                    print(f"Found collection of {len(tokenData['collection'])} elements")
                    if "type_mime" in tokenData["properties"]:
                        print(f"Type : {tokenData['properties']['type_mime']}")
                        ext = tokenData["properties"]["type_mime"].split("/")[1]
                    else:
                        print("Unknown type")
                        ext = "data"
                    
                    dirname = re.sub(r'[^\w\d-]','_', tokenData["name"])[:20] + "_" + args[0]

                    os.mkdir(dirname)

                    for i in range(len(tokenData['collection'])):
                        filename = dirname + "/" + str(i) + "_" + re.sub(r'[^\w\d-]','_', tokenData['collection'][i]['name'])[:20] + "." + ext

                        with open(filename, "wb") as f:
                            f.write(Token.dumpContent(tokenData['collection'][i]["content"]))
                            print(f"Saved {i + 1}/{len(tokenData['collection'])} : {filename}")
            else:
                Token.printToken(api.getToken(args[0]), args[1].lower() == "full" if len(args) >= 2 else False)
    
    def dumpContent(contentData):
        if "raw" in contentData:
            return base64.b64decode(contentData["raw"].encode("ascii"))
        elif "ipfs" in contentData:
            link = contentData["ipfs"]
            if not link.startswith("ipfs://"):
                raise ValueError(f"Invalid ipfs link : {link}")
            
            tmp = link[7:].split("/", 1)
            if len(tmp) != 2:
                raise ValueError(f"Invalid ipfs link 2 : {link}")
            
            # req = requests.get(f"https://{tmp[0]}.ipfs.dweb.link/{tmp[1]}")
            req = requests.get(f"https://ipfs.io/ipfs/{tmp[0]}/{tmp[1]}")
            return req.content
        else:
            raise Exception("Unknown content type : " + str(contentData.keys()))

    def printToken(tokenData, fullCollection = False):
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
        
        if "collection" in tokenData and len(tokenData["collection"]) > 0:
            print(f"{len(tokenData['collection'])} collection elements :")

            for i, c in enumerate(tokenData["collection"]):
                if not fullCollection and i >= 3:
                    print("[...] Use \"full\" argument to show all")
                    break

                print(json.dumps(c, indent=4))