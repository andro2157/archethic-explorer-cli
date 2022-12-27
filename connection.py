import requests
# import aiohttp
import json

from exceptions import QueryError

ARCHETHIC_MAINNET = "https://mainnet.archethic.net"
ARCHETHIC_TESTNET = "https://testnet.archethic.net"

class Connection:
    def __init__(self, endpoint = ARCHETHIC_MAINNET):
        self.endpoint = endpoint
    
    def executeQuery(self, query):
        req = requests.post(self.endpoint + "/api", headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }, data = json.dumps({"query": query}))

        req.raise_for_status()

        req_json = req.json()
        
        if "errors" in req_json:
            raise QueryError(req_json["errors"], query)
        
        return req_json

    # async def asyncExecuteQuery(self, query, session: aiohttp.ClientSession):
    #     async with session.post(self.endpoint + "/api", data = json.dumps({"query": query})) as req:
    #         req_json = await req.json()
    #         if "errors" in req_json:
    #             raise QueryError(req_json["errors"], query)
            
    #         return req_json

con = Connection()