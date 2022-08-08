# Modules : are simply files with the '.py' format containing python code that can be imported inside another python program

# Consider a Module the same as a 'code library' that contains a set of functions that can be re-used in another program

# Modules can be of two type : 'built-in' module and 'user-formed' module

# To incorporate the module into a program use the 'from' keyword and to get functions from a module use the 'import' keyword


# Using a built-in module :


# Command 'ctrl + space' on keyboard to see the list of all functions of a module

from math import pow  # Then select a DESIRED FUNCTION directly from the list to work on

four_cube = pow(4, 3)

print(four_cube)


# Or,


from math import *  # Use * (asterisk sign) to import ALL THE FUNCTIONS from a module

Two_cube = pow(2, 3)  # Then select the specific function (here, power) to work on

print(Two_cube)



