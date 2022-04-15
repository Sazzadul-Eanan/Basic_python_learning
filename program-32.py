# Finding the sum of a sequence ( 2, 4, 6....n ) using 'while-loop' and 'input' from the user

n = int(input('Enter the last term : '))       # 'int' for integer

sum = 0
i = 2
while i <= n :         # 'n' is the last term of the sequence up to which all the numbers will be added
    sum = sum + i
    i = i + 2

print (sum)