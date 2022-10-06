# PARAMETERS and ARGUMENTS are used for passing data into the function

# PARAMETER-

# A parameter is a variable defined as part of the function header and is used to make data available within the function itself.
# Once A parameter has a default value all remaining parameters to the 'right' of that parameter must also have default values.
# To define a parameter list as being of arbitrary length, a parameter is marked with an asterisk (*).

def add(x, y):      # x,y are parameters
 sum = x + y        # The 'function body' defines what the function does
 print(sum)

add(25, 75)         # calling the functions