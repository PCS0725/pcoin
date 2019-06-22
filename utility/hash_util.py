import hashlib as hl
import json

def hash_string_256(string):
    """Create a SHA256 hash for a given input string.
    creates a 32 byte(256 bit) hash for the given string 

    Arguments:
        :string: The string which has to be hashed.
    """
    return hl.sha256(string).hexdigest()


def hash_block(block):
    """Hashes a block and returns a string representation of it.

    Arguments:
        :block: The block that should be hashed.
    """
    #Convert the block object to a dictionary and store it in a copy variable
    hashable_block = block.__dict__.copy()
    #The transactions in the block object are also objects
    #They are converted into dictionaries
    hashable_block['transactions'] = [tx.to_ordered_dict() for tx in hashable_block['transactions']]
    return hash_string_256(json.dumps(hashable_block, sort_keys=True).encode())