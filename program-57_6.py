# Global variable is a variable which is not defined inside any function
# Its scope is throughout the program and inside every function


x = 'My name is Fahim'          # global scope

def name ( ) :
                          # As there is no local variable, the value from the global variable will be used

    print(x)              # Inside the function's indent

name()                    # caller / driver code



print(x)                  # Outside the function's indent