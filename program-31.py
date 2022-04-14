# Finding the sum of 'n' numbers using 'while-loop' and 'input' from the user

n = int (input('Enter the last term : '))    # 'int' for integer

sum = 0
i = 1
while i <= n :     # 'n' is the last term of the sequence upto which all the numbers will be added
    sum = sum + i
    i = i + 1
print (sum)