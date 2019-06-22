import hashlib
from utility.hash_util import hash_block
from wallet import Wallet

class Verification:
    """Used as a helper class by grouping functionalities.
    NO Object instantiation is reqd. All the functions are either static or class methods.
    They receive their arguments from outside"""

    #Static methods do not require class variables as well
    @staticmethod
    def valid_proof(transactions,last_hash,proof):
        """Checks whether a proof_of_work is valid or not
        Arguments :
        transactions: The list of transactions to be mined
        last_hash : The has value of previous block
        proof : The number with which we generate a hash"""
        guess=(str([tx.to_ordered_dict() for tx in transactions])+str(last_hash)+str(proof)).encode()
        guess_hash=hashlib.sha256(guess).hexdigest()
        #Check the validity of generated hash under a predefined condition
        return guess_hash[0:2]=='00'

    #Class methods require access to class variables or methods
    @classmethod
    def verify_chain(cls,blockchain) :
        for (index, block) in enumerate(blockchain):
            if index == 0:
                continue
            #Matches the generated and saved hashes for each block
            if block.previous_hash != hash_block(blockchain[index - 1]):
                return False
            #regenerates the proof and verifies the chain
            if not cls.valid_proof(block.transactions[:-1], block.previous_hash, block.proof):
                print('Proof of work is invalid')
                return False
        return True

    @staticmethod
    def verify_transaction(transaction,get_balance,check_funds=True):
        #Verifies if a transaction is valid or not
        #Check funds will be False when all open transactions are being verified altogether
        #This is done to avoid checking balances again and again 
        if(check_funds==True):
            sender_balance=get_balance(transaction.sender)
            return (sender_balance>=transaction.amount and Wallet.verify_transaction(transaction))
        else:
            return Wallet.verify_transaction(transaction)

    @classmethod
    def verify_transactions(cls,open_transactions,get_balance): 
        """Verifies all open transactions."""
        return all([cls.verify_transaction(tx,get_balance,False) for tx in open_transactions])
