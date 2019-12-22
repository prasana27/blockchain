class Block:
    """
    Block: a unit of storage
    Store of transactions in a blockchain that supports cryptocurrency
    """
    def __init__(self,data):
        self.data = data

    def __repr__(self):
        return f'Block_data: {self.data}'

def main():
    block = Block('pk')
    print(block)
    print(f'block.py __name__: {__name__}')

if __name__ == '__main__':
    main()