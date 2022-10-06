# Lambda function - is an anonymous function of just a single line of code
# A FUNCTION FOR USING ONLY ONCE; giving it a name for this one time can pollute the namespace of the program
# Lambda functions can have ANY NUMBER OF ARGUMENTS but only 'ONE STATEMENT' to execute

# Create a program to calculate the value of the formula '(a+b)**2'

'''
def calculate (a, b) :
    ans = a*a + 2*a*b + b*b
    print(ans)

calculate(3,5)
'''

# the above one is a normal function, but the following is a 'lambda' version of it

   # (lambda    parameters    :    executable statement)       (call)               # format of a lambda function

x = (lambda   a,b   :   a*a + 2*a*b + b*b)   (2,3)
print(x)


