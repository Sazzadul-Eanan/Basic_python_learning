# Use of 'continue'
# 'continue' can't work without 'if condition'

i = 1
while i <= 20 :    # This part of the code is to print all the numbers up to 20
    if i == 10 :
        continue   # This part of the code is to print all the numbers up to 9 because, when the 10 comes (i == 10) the printing will be stopped but never jumps to the next 'print'
    print(i)
    i = i + 1

print("FAHIM")