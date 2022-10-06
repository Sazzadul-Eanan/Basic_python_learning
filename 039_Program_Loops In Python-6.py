# Finding the sum of 'n' numbers using 'while-loop' and 'input' from the user


n = int(input('Enter the last term :- '))      # 'int' is for integer conversion of input 'numerical values as string'

sum = 0
i = 1
while i <= n :          # 'n' is the last term of the sequence up to which all the numbers will be added
    sum = sum + i
    i = i + 1
print(sum)




# Finding the sum of 'n' numbers using 'for-loop' and 'input' from the user


n = int(input('Enter the last term :- '))

sum = 0
for i in range(n+1) :
    sum = sum + i
print(sum)