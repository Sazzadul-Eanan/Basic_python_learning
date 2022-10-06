# Use of some important 'functions' of list

# list1 = ['RABBI','SAKA','NOYON','ADIL']

# list2 = [100, 40, 40, 10, 65]

'''
list1.sort()      # to sort the 'list1' alphabetically      # this function is applicable only when all the items of a list are of simillar data type
print(list1)
'''
'''
list1.reverse()   # to reverse the position of the items of 'list1' based on index value order
print(list1)
'''
'''
list2.sort()      # to sort the 'list2' in ascending order
print(list2)
'''
'''
list3 = list1.copy()    # copy 'list1' in a new 'list3'
print(list3)
'''
# list4 = [38, 45, 76, 38, 99, 38, 71, 38, 46, 38]
'''
x = list4.count(38)     # to count the frequency of a definite item in a list
print(x)                # x is nothing but a variable here
'''
'''
list2.extend(list4)     # to extend list2 with all the items of list4 at the end 
print(list2)
'''

tup = (5, 7, 'Ross', 8, 4, 'Phoebe')       # other collection type to 'list' conversion
lis = list(tup)
print(lis)