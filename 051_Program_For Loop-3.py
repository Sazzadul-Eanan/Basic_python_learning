# Sum of a multiplied series

    # 1 x 2 x 3 x ... x n

n = int(input("Enter the last number :- "))

sum = 1                          # sum is not '0' for this type of multiplied series
for x in range (1, n+1) :        # 1 is the lower limit, n+1 is the upper limit of the series
    sum = sum * x                # if the sum were '0' here, then the whole sum will be '0' after the multiplication

print(sum)