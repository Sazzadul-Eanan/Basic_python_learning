# Sum of a multiplied series
    # 1 x 2 x 3 x ... x n x n

n = int(input("Enter the last number :- "))
sum = 1                          # not '0' for this type of series
for x in range (1, n+1, 1) :     # 1 is the lower limit, n+1 is the upper limit and 1 is the interval of the series
    sum = sum * x

print(sum)