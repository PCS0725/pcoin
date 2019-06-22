from Crypto.PublicKey import RSA
import Crypto.Random
import binascii
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256

class Wallet:
    """To create a set of public-private keys for a node
       They are used to create a signature and verify that signature for each transaction"""
    def __init__(self,node_id):
        self.private_key=None
        self.public_key=None
        self.node_id=node_id
    
    def create_keys(self):
        """Executed when wallet is created"""
        private_key,public_key=self.generate_keys()
        self.private_key=private_key
        self.public_key=public_key
       

    def load_keys(self):
        """Loads the keys from file,if they exist and assigns them to attributes"""
        try :
            with open('wallet-{}.txt'.format(self.node_id),mode='r') as f:
                keys=f.readlines()
                public_key=keys[0][:-1]
                private_key=keys[1]
                self.public_key=public_key
                self.private_key=private_key
                return True
        except(IOError,IndexError):
            print('Loading wallet failed')
            return False


    def generate_keys(self):
        """Generates a set of keys when the wallet is created ."""
        private_key=RSA.generate(1024,Crypto.Random.new().read)
        public_key=private_key.publickey()
        return (binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii'),binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii'))
    
    def save_keys(self):
        if self.public_key!=None and self.private_key!=None:
            try :
                with open('wallet-{}.txt'.format(self.node_id),mode='w') as f:
                    f.write(self.public_key)
                    f.write('\n')
                    f.write(self.private_key)
                    return True
            except:
                print('Saving keys failed')
                return False
    
    def sign_transaction(self,sender,recipient,amount):
        """Returns a signature for a given transaction,which is the passed to add transaction function"""
        signer = PKCS1_v1_5.new(RSA.importKey(binascii.unhexlify(self.private_key)))
        #payload
        h=SHA256.new((str(sender)+str(recipient)+str(amount)).encode('utf8'))
        signature=signer.sign(h)
        return binascii.hexlify(signature).decode('ascii')

    @staticmethod     
    def verify_transaction(transaction):
        """Verifies the signature of transaction using the public key"""
        binary=binascii.unhexlify(transaction.sender)
        public_key=RSA.importKey(binary)
        verifier=PKCS1_v1_5.new(public_key)
        h=SHA256.new((str(transaction.sender)+str(transaction.recipient)+str(transaction.amount)).encode('utf8'))
        return verifier.verify(h,binascii.unhexlify(transaction.signature))