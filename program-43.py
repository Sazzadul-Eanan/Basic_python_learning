# Finding a 'prime' number from user input

n = int(input('Enter the number :- '))
for i in range (2, n) :    # 'i' is the range of numbers from 2 to (n-1), where 'n' is the input by the user
    if n % i == 0 :        # when 'n' is divided by all the values of 'i' then, if the remainders is '0' only then the 'n' is a prime
        print('Not prime')
        break

else :
    print('Prime')