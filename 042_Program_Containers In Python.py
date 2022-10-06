# There are four classes in Python that provide container like behaviour; that is data types for holding collections of other objects, these are - Tuples,  Lists,  Sets,  Dictionary

# TUPLE ( )

# It is not possible to ADD or REMOVE elements from a Tuple; they are IMMUTABLE.

tup1 = (6, 5, 8, 'plum', 7, 4, 'apple')           # USE 'ROUND BRACKET'

print(tup1[2])               # accessing the elements of a Tuple using index value

print(tup1[1:3])             # slicing a Tuple using index value

print(len(tup1))             # length of a Tuple

print(tup1.index('plum'))           # find the index of an item in a Tuple

list1 = [1, 2, 3]
tup = tuple(list1)           # transforming other collection type to 'Tuple'
print(tup)



# Nested Tuples

tuple1 = (1, 3, 5, 7)
tuple2 = ('John', 'Denise', 'Phoebe', 'Adam')
tuple3 = (42, tuple1, tuple2, 5.5)

print(tuple3)

# In fact, a Tuple can have nested within it not just other Tuples but any type of container, and thus it can contain Lists, Sets, Dictionaries etc.