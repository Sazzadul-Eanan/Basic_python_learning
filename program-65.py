# Lamda function - is an anonymous function of just a single line of code
'''
def calculate (a,b) :
    return a*a + 2*a*b + b*b
print(calculate (2,3))
'''

# the above one is a normal function, but the following is a 'lamda' version of it

  # lambda  parameter : expression                   # format of a lamda function

x = (lambda  a,b : a*a + 2*a*b + b*b) (2,3)
print(x)


