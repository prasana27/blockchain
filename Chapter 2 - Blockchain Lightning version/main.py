class Block:
    def __init__(self, data, hash, last_hash):
        self.data = data
        self.hash = hash
        self.last_hash = last_hash


foo_block = Block('foo_data', 'foo_hash', 'foo_last_hash')


print(foo_block.data)
print(foo_block.hash)
print(foo_block.last_hash)
