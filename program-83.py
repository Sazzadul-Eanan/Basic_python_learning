# Map function takes 2 things simultaneously : a 'function' and a 'list'
# Map function always works with iterable object specially 'list'
# It is the functional equivalent of a 'for-loop' applied to an iterable
# Map applies the defined function to all items in the iterable passed to it
# Map function gives 'output' as an iterable object


# Create a program for getting 'squared' values of a list of numbers


def square(x) :                       # A function
    return x*x                        # 'x' is a variable for passing the items of iterable into the function as like as for loop

num = [1, 2, 3, 4, 5, 6]              # A list / iterable

ans = list(map(square,num))           # Passing the 'function' and the 'iterable' into map()
                                      # 'list()' for relisting the returned values

print (ans)