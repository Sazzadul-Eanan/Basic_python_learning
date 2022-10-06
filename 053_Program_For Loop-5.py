# Finding all the 'prime' within an interval of number from user input

# First condition is 1 is not a prime so take all the numbers greater than 1

# Second condition is the number which is not a 'prime' will be divisible by any number less than it

start = int(input('Enter the starting number :- '))
end = int(input('Enter the ending number :- '))

for num in range (start , end + 1) :
    if num > 1 :                              # condition-1
        for i in range (2, num) :
            if num % i == 0 :                 # condition-2
                break

        else :
            print(num)