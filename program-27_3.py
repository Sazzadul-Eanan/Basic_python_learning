# Continue - this allows you to skip over some part of a loop’s iteration for a particular value, but then to continue with the remaining values in the sequence.

# 'continue' can't work without 'if condition'

# For-loop : continue


for x in range (1 , 8) :

    if x == 4 :                    # skip over 4
        continue
    print(x)