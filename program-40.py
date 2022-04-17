# Finding the 'sum' of a series from user input using 'for loop'
         # 1 + 2 + 3 + 4....+ n

n = int(input("Enter the last number :- "))
sum = 0
for x in range (1, n+1, 1) :     # 1 is the lower limit, n+1 is the upper limit and 1 is the interval of the series
    sum = sum + x                # here n+1 is because the use of 'range'. as in range function to get the output 'n' the upper limit should be 'n+1'
                                 # to better understand 'range function' see program-38 again
print(sum)

