# Sum of an exponential series
    # 1*2 + 2*2 + 3*2 + ... + n*n

n = int(input("Enter the last number :- "))
sum = 0
for x in range (1, n+1, 1) :     # 1 is the lower limit, n+1 is the upper limit and 1 is the interval of the series
    sum = sum + x*x              # x*x means the square function, such as 3 squared is actually 3*3, 4 squared is 4*4, etc.

print(sum)