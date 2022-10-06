# Local and global variable / scope is 'sometimes' all about indentation

# x = 'What is the variable ?'              # Global

''''
def void () :
    x = 'What is the variable ?'            # local

# x = 'What is the local variable ?'        # Global

    print (x)                               # Local printer

# x = 'What is the variable ?'              # Global

void()

print (x)                                   # Global printer

'''

# To use the global variable in 'local-scope' the keyword 'global' is used

def void () :
    global x

    print (x)

x = 'What is the variable ?'                # Global

void()