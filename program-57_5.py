# Local variable and Global variable for a function

# A local variable is a variable which is defined inside a function
# Its scope is limited to that function only


def name ( ) :
    x = 'My name is Fahim'          # local scope
    print(x)
name()


'''
# A local variable is not usable outside the function

def name ( ) :
    x = 'My name is Fahim'
    print(x)                        # Inside the function's indent 
name()

print(x)                            # Outside the function's indent 
'''