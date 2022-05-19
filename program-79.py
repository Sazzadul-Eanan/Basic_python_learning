# Method Overriding : is the process through which an 'inheriting method' can be replaced by a 'new method' of the relevant class

# Inheriting Method : the method which has been taken from the 'parent class' by a 'child class'

class phone :
    def __init__(self) :
        print ('I am in phone class.')

class nokia (phone) :                          # inheriting the method from the class 'phone'
    def __init__(self) :                       # new method to override
        print('I am not in phone class')

phone()

nokia()

# Without overriding the 'I am in phone class' message would be printed