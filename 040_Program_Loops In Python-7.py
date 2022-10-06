# Finding the sum of a sequence ( 2, 4, 6....n ) using 'while-loop' and 'input' from the user

n = int(input('Enter the last term :- '))

sum = 0
i = 2
while i <= n :         # 'n' is the last term of the sequence up to which all the numbers will be added
    sum = sum + i
    i = i + 2

print (sum)



# Finding the sum of a sequence ( 2, 4, 6....n ) using 'for-loop' and 'input' from the user

n = int(input('enter the last term : '))

sum = 0
for i in range (2, n+1, 2) :
    sum = sum + i

print(sum)