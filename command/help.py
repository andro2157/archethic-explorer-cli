from command.command import Command

class Help(Command):
    def __init__(self):
        super().__init__()
    
    def userInput(self, args):
        super().userInput(args)

        print("""
        - balance <address> (exact) : gets the balance of an addresss. With the 'exact' option, it won't seek for the last address
        - chain <address> (pagingaddress) : query the network to find a transaction chain
        - endpoint <nearest,mainnet,testnet,list,custom> (custom url)
        - help
        - last <address> : gets the last transaction from an address
        - nodes : list all the nodes registered in the network
        - oracle (timestamp) : gets oracle price
        - query (query) : custom graphql query. Multiline input if no query is provided
        - token <address> (dump, full) : gets the info of a token. Can dump the NFT content or collection
        - transaction <address> (raw) : gets the info of a transaction
        - transactions (page) : query the network to find all the transactions locally stored
        - type <type> (page) : query the network to list the transaction on the type
        """)