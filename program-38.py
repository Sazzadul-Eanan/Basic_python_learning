# Range is a function when use within the list function can generate a 'list' of a range of number

'''
x = list(range(10))

print(x)
'''

'''
# For a well defined 'limit' of the range

x = list(range(5, 10))       # 5 is the lower and 10 is the upper limit

print(x)
'''

# For a well defined 'limit' of the range and 'interval' between the printed numbers

x = list(range(2, 15, 3))     # 2 is the lower limit, 15 is the upper limit and 3 is the 'interval'
                              # 'range' is not inclusive, means for 'n' upper limit it generates the highest value of 'n-1'
print(x)