# Recursion is a process where a function can call itself again and again

# after the job is done the 'recursive call' can be stopped by the 'base case'

# program to get the value of 5!

# background theory   :   n! = n * (n-1)!                # 5! = 5 * 4!

def fact(n) :
    if n == 1 :        # base case
        return 1
    else :
        return n * fact(n-1)

x = fact(5)

print(x)
