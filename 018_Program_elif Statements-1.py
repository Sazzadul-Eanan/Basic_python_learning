# elif statement-

# elif statement commands the program to try another condition if the previous one is not true

# Remember in 'elif' statement, if any of the conditions above 'elif' works, then rest of the conditions below that 'elif' will not work

marks = 65

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