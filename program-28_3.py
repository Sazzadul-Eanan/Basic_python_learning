# Basic difference between 'for' & 'while' loop

# Loop over a set of values in a range (of 1 to 5) using both 'for' & 'while' loop


i = 1                 # here 'i' is a variable and it needs to have a value  for the 'first iteration' of the while loop
                      # before the while loop does anything 'the program' needs to already know the first value of count so that it can perform that very first test
while i <= 5 :        # in a 'while loop' the iteration starts from the value as it is declared in the 'initialization' such as 'i = 1'
    print(i)          # in 'while loop' number of iterations is not known but, the conditions for stopping is known
    i = i + 1         # this iteration is used when the number of times we need to repeat the 'block of code' to execute is not known



'''
for i in range(1, 6) :      # in 'for loop' the range-iteration always increase 1 by 1, up to 'n-1' (where n = range)
    print(i)                # in 'for loop' number of iterations is known
                            # 'range' is actually a function that generates the range of values to be used as the sequence in the 'for loop'
                            # No need to define the loop variable first.
                            # the code is more concise
'''