class Printable:
    """Whenever an object is printed ,of any class, we can define the dunder(__funcName__)
    __repr__ to specify what should be output and what not"""
    def __repr__(self):
        #makes a string of the dictionary and returns it
        return  str(self.__dict__)