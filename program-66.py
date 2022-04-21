# Map function can process 2 different type parameter simultaneously (a 'function' and a 'list')

# program for getting 'squared' values of a list of numbers

def square(x) :               # function
    return x*x
num = [1, 2, 3, 4, 5]         # list

result = list(map(square,num))       # 'list()' for relisting the returned 'squared' values

print(result)