from backend.blockchain.block import Block

class Blockchain:
    """
    Blockchain: a public ledger of transaction
    Implemented as a list of blocks - data sets of transactions
    """

    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        last_block = self.chain[-1]
        self.chain.append(Block.mine_block(last_block, data))
    
    def __repr__(self):
        return f'Blockchain: {self.chain}'

    @staticmethod
    def is_valid_chain(chain):
        """
        Validate the incoming chain
        Ensure these rules are followed for blockchain:
            - The first block of the chain must be the genesis block
            - The blocks must be formatted correctly
        """
        if chain[0] != Block.genesis():
            raise Exception('The geneis block must be valid')

        for i in range(1, len(chain)):
            block = chain[i]
            last_block =  chain[i-1]
            Block.is_valid_block(last_block,block)


def main():
    blockchain = Blockchain()

    blockchain.add_block('one')
    blockchain.add_block('two')
    
    print(blockchain)
    print(f'blockchain.py __name__:{__name__}')

if __name__ == '__main__':
    main()



