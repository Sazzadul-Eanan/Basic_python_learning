# Set { }

# set is IMMUTABLE
# set is an unordered(UN-INDEXED) collection of item
# items of set can not be accessed with 'index' value
# DUPLICATE value is not allowed
# can be created with 'CURLY BRACKET' or 'set' function


s1 = {1, 2, 3, 4}

print(s1)

'''
print(3 in s1)       # check the existence of a number in a set
'''
'''
print(len(s1))       # length of the set 
'''
'''
s1.add(9)            # add new item into a set
print(s1)
'''
'''
s1.remove(2)         # remove item from a set 
print(s1)
'''
'''
print(max(s1))       # maximum value of the set 
'''
'''
print(min(s1))       # minimum value of the set
'''
'''
s2 = [100, 200, 300, 400]        # here s2 is a list
s3 = set(s2)         # conversion from other data structure to 'set' using set function
print(s3)
'''