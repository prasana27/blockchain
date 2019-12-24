from backend.util.crypto_hash import crypto_hash

def test_crypto_hash():
    # It should create the same hash with arguments of different data types in any order

    assert crypto_hash(1,[2],'three') == crypto_hash([2],1,'three')
    assert crypto_hash('pk') == '6ded23596234c2e44755814ebda190318ed47845ff95b8e65509d394430a9577'
    
