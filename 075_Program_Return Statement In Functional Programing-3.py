# Create a program to find the greatest number between three numbers

def greatest (x, y, z) :
    if x > y and x > z :
        return x
    elif y > x and y > z :
        return y
    else :
        return z

ans = greatest(456,765, 123)

print('The greatest number is : ', ans)

