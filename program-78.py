# Inheritance : is the process through which 'some existing methods' of a class is brought into another class

# Main purpose of 'inheritance' is to re-use the existing methods of a class into another class


class phone :                                     # parent class / super class / base class
    def call (self) :                             # (notice the sign beside code's serial no.)
        print('You can call.')
    def message (self) :
        print('You can message.')

                                                  # child class / sub class / derived class
class xiaomi (phone) :
    def photo (self) :                            # '(phone)' means importing the methods of 'phone' into the class 'xiaomi'
        print('You can take photo.')

# Now the class 'xiaomi' is inheriting the methods of class 'phone'

x = xiaomi()                                      # creating object
                                                  # calling both the method individually
x.call()
x.message()


