# Create a program to add 1 (one) with all the numbers of a list of number

data = [20, 30, 40, 50, 60]

def add_one(x):
  return x + 1


ans = list(map(add_one, data))

print(ans)