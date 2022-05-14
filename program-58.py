# Return statement in function

# The return statement is used inside a function to send the function’s result back to the 'caller code'
# Return statement can not be used outside the function
# The statements after the return statement are not executed

def add (x,y) :
    sum = x + y
    return sum

result = add(23,27)         # caller code
                            # result is the variable to store the returned sum

print(result)
