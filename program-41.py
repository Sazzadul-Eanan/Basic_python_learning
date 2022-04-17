# Sum of an exponential series
    # 1*2 + 2*2 + 3*2 + ... + n*n

n = int(input("Enter the last number :- "))
sum = 0
for x in range (1, n+1, 1) :     # 1 is the lower limit, n+1 is the upper limit and 1 is the interval of the series
    sum = sum + n*n

print(sum)