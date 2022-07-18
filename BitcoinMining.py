from hashlib import sha256  #to convert text into 256 bit (64bit Hexa Digit)
import time

MAX_NONCE = 10000000  #to iterate to find the nonce value to match the prefix zeros


def SHA256(text):
    """
    It converts the text into encoded string.
    """
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    """
    A block in a blockchain consists of block number, transactions and old hash.
    nonce - number once
    When nonce (a particular digit) is added with block number, txns, and old hash,
    a new hash will be generated.
    We need to find that nonce to match the new hash with given number of prefix zeros.
    """
    prefix_str = prefix_zeros*"0"
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print("Yay! successfully mined bitcoins with nonce value: {}".format(nonce))
            print("New Hash: ", new_hash)
            return new_hash
    raise BaseException(f"Couldn't find the correct hash value after tried {MAX_NONCE} times.")

if __name__=='__main__':
    transactions='''
    tony->tom->56
    steve->john->34
    '''
    previous_hash = "yytytyt6756r5yt6rtyftyt67t675t67tygyt6rrefgujhuyg6t56gyg"
    prefix_zeros = 8
    start_time = time.time()  #it stores the current time in a variable during the start of execution
    new_hash = mine(5, transactions, previous_hash, prefix_zeros)
    end_time = time.time()  #it stores the current time in a variable during the end of execution
    total_time = end_time - start_time

    print(f"Total time taken: {total_time:.6f} seconds")
