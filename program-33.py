# Create a program to take the range input from the user and add all the numbers in between the range



start = int(input('Enter the starting number :  '))
end = int(input('Enter the ending number :  '))

'''
# using the while loop -

sum = 0
i = start

while i <= end :
    sum = sum + i
    i = i + i
print (sum)
'''


# using the for loop -


sum = 0

for i in range (start, end+1) :
    sum = sum + i
print(sum)