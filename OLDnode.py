#test file used to test the code on the terminal
from uuid import uuid4

from wallet import Wallet
from blockchain import Blockchain
from utility.verification import Verification

class Node :
    """Each device on the blockchain network.
    It will have its own copy of the blockchain."""
    def __init__(self):
        #self.id=str(uuid4())
        self.wallet=Wallet()
        self.blockchain=None
        self.wallet.create_keys() 
        #Blockchain is initialised in our code only when user has a wallet
        self.blockchain=Blockchain(self.wallet.public_key)

    def get_transaction_data(self) :
        """Gets the user input and return it in a tuple"""
        tx_recipient=input("Enter the receiver : ")
        tx_amount=float(input("Enter the number of coins : "))
        return (tx_recipient,tx_amount)

    def listen_for_input(self):
        waiting_for_input=True
        while waiting_for_input :
            print('Enter your choice :')
            print('1.Make a new transaction')
            print('2. Mine a new block ')
            print("3.Print all the blocks")
            print('4.Create wallet')
            print('5.Load wallet')
            print('6.Save keys')
            print("7.Quit")
            user_choice=input()
            if user_choice=='1' :
                #Take the user input and store it in a tuple
                tx_data=self.get_transaction_data()
                #unpack the tuple here and pass the arguments
                recipient,amount=tx_data
                signature=self.wallet.sign_transaction(self.wallet.public_key,recipient,amount)
                #We need a named argument since sender is the second field in the function definition
                if self.blockchain.add_transaction(recipient,self.wallet.public_key,signature,amount=amount) :
                    print("Transaction added successfully")
                else :
                    print("Insufficient Balance of sender")

            elif user_choice=='2' :
                #Will fail if user does not have a wallet(public key)
                if not self.blockchain.mine_block():
                    print('Mining failed ! Got not wallet ? ')
                    print('Or, One or multiple transaction were modified !')

            elif user_choice=='3':
                print(self.blockchain.get_chain())

            elif user_choice=='4':
                self.wallet.create_keys() 
                #Blockchain is initialised in our code only when user has a wallet
                self.blockchain=Blockchain(self.wallet.public_key)

            elif user_choice=='5':
                self.wallet.load_keys()
                self.blockchain=Blockchain(self.wallet.public_key)

            elif user_choice=='6':
                self.wallet.save_keys()

            elif user_choice=='7' :
                waiting_for_input=False

            else :
                print("Invalid input,please input a valid value from the choices !")

            """Check the validity of blockchain after each user operation"""
            if not Verification.verify_chain(self.blockchain.get_chain()):
                print('Invalid blockchain!')
                # Break out of the loop
                break
            print('Balance of {} is {:6.2f}'.format(self.wallet.public_key,self.blockchain.get_balance()))
if __name__=='__main__':
    node1=Node()
    node1.listen_for_input()