# Finding the greatest number among the three numbers using 'nested_if'

num1 = 30
num2 = 20
num3 = 40

if num1 > num2 :
   if num1 > num3 :
     print(num1)
   else :
       print(num3)
if num2 > num1 :     # Or you can barely use 'else :' here
    if num2 > num3 :
        print(num2)
    else :
        print(num3)



