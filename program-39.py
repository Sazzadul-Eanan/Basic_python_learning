# Accessing list items using 'while' and 'for' loop

list = [20, 30, 40, 50, 60]

'''
# To apply 'while loop' here, the idea of 'index value' is must

i = 0                 # 'i' is the index value , starts from '0'
while i <= 4 :        # here 4 is the highest 'index value'
    print(list [i])
    i = i + 1
'''
# But to apply 'for loop' here, the idea of 'index value' is not necessary

for x in list :       # 'x' is a variable
    print(x)