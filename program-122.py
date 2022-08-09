# Exception Handling

# Exception : An exception in Python is AN INCIDENT that happens while executing a program that causes the regular course of the program's commands to be disrupted
# When a Python script raises an exception, it must either handle the exception immediately otherwise it terminates and crash the program and doesn't perform the subsequent codes
# Try and Except statements are used to catch and handle exceptions in Python.

# Exception Handling of A User-defined Function While Performing Division

'''
def divide (x, y) :
    return x / y

print (divide(10, 2))
print (divide(3, 0))            # 2ND call
print(divide(9, 3))
'''

# If we run this program, we will get only one answer from the 1ST call of the program, and then when the program will proceed to the 2ND call it will terminate the program.
# This is because the mathematical rule (EXCEPTION) of "No number can be divided by the number zero (0)."
# Now if we can handle this exception, we can avoid the crashing of the program and get the program efficient for the subsequent CALLS.

def divide (x, y) :
    try :
        return x / y
    except ZeroDivisionError :
        print('Can Not Divide By Zero')

print (divide(10, 2))
print (divide(3, 0))              # 2ND call
print(divide(9, 3))