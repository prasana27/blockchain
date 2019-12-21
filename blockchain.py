class Block:
    """
    Block: a unit of storage
    Store of transactions in a blockchain that supports cryptocurrency
    """
    def __init__(self,data):
        self.data = data



class Blockchain:
    """
    Blockchain: a public ledger of transaction
    Implemented as a list of blocks - data sets of transactions
    """

    def __init__(self):
        self.chain = []

    def add_block(self, data):
        self.chain.append(Block(data))