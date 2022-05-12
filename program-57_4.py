# PARAMETERS and ARGUMENTS are used for passing data into the function

# ARGUMENT-

# An argument is the actual data passed into the function when it is called.
# This data (argument) will be held within the parameters.

# X-arguments
# the way through which we can pass as many 'parameters' as we want within a 'function' without declaring any of the 'parameters'

def student (*details) :        # details is only a variable but the *(asterisks) play the role of 'arguments'
    print(details)

student('Fahim')
student(1001, 'Fahim')
student(1001, 'Fahim', 'Male')