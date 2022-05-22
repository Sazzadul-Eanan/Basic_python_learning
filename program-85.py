# Filter function can filter out items, based on some 'conditions' assigned on an iterable
# Filter function always works with iterable object specially 'list'
# the condition-unmatched 'items' will be removed


# Create a program for getting 'even' values from a list of numbers


def even (x) :
   return x % 2 == 0

num = [1, 2, 3, 4, 5, 6]

result = list(filter(even,num))         # 'list()' for relisting the returned values

print(result)