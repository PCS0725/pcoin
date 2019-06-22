from collections import OrderedDict
from utility.printable import Printable

class Transaction(Printable):
    def __init__(self,sender,receiver,signature,amount):
        self.sender=sender
        self.recipient=receiver
        self.amount=amount
        self.signature=signature
        
    def to_ordered_dict(self):
        return OrderedDict([('sender',self.sender),('recipient',self.recipient),('amount',self.amount)])