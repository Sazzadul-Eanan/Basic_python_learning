# Filter function can filter an 'object' based on some assigned 'conditions'
# the condition-unmatched 'items' will be vanished

# program for getting 'even' values of a list of numbers

def even (x) :
   return x % 2 == 0

num = [1, 2, 3, 4, 5]

result = list(filter(even,num))      # 'list()' for relisting the returned 'squared' values

print(result)