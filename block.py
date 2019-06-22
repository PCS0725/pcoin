from time import time
from utility.printable import Printable

class Block(Printable):
    """Defines the blueprint of each block in the blockchain"""
    def __init__(self,index,previous_hash,transactions,proof,time=time()) :
        self.index=index
        self.previous_hash=previous_hash
        self.transactions=transactions
        self.timestamp=time
        self.proof=proof
   