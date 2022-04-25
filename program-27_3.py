# Continue - this allows you to skip over part of a loop’s iteration for a particular value, but then to continue with the remaining values in the sequence.


# For-loop : continue


for x in range (1 , 6) :

    if x == 4 :                    # skip over 4
        continue
    print(x)