# list as input (string) from user

x = input('Enter a text of numbers :- ')

list = x.split()     # split function converts the 'text' format of numbers as 'list' format
sum = 0

for i in list :
    sum = sum + int(i)

print(sum)

