# elif statement-

# A Letter grade program using 'elif' statement, working upon user input

marks = int(input("Enter the obtained marks :- "))

if marks >= 80 :
    print('A+')
elif marks >= 70 :
    print('A')
elif marks >= 60 :
    print('A-')
elif marks >= 50 :
    print('B')
elif marks >= 40 :
    print('C')
elif marks >= 33 :
    print('D')

else:
    print('Fail')