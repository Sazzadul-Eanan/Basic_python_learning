# Zip function can convert so many 'list' into a single list (of tuples)

id = [101, 102, 103, 104, 105]
name = ['Fahim','Karim','Rahim','Fokir','Tokir']
country = ['China', 'India', 'France', 'Mali', 'Chad']

x = list(zip(id, name, country))
print(x)