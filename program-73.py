# Return statement in function

# The return statement is used inside a function to send the function’s result back to the 'CALLER CODE'
# Return statement can not be used outside the function
# The statements after the return statement are not executed

def add (x,y) :
    sum = x + y
    return sum

result = add(23,27)         # CALLER CODE
                            # result is THE VARIABLE TO STORE the returned sum

print(result)



'''
def add (x, y) :
    sum = x + y
    return sum

result_1 = add(35, 65)
result_2= add(990, 5)

print("Result one is = ", result_1)
print("Result two is = ", result_2)
'''