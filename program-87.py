# Zip function can convert so many 'list' or 'tuple' into a single list (of tuples)
# It returns an iterator, from two or more iterators

id = [101, 102, 103, 104, 105]
name = ['Fahim','Karim','Rahim','Fokir','Tokir']
country = ['China', 'India', 'France', 'Mali', 'Chad']

x = list(zip(id, name, country))
print(x)




# If one list or tuple contains more items than the others, these items are ignored

id = (101, 102, 103, 104, 105)
name = ('Fahim','Karim','Rahim','Fokir','Tokir', 'Sogir', 'Mogir')

x = list(zip(id, name))
print(x)