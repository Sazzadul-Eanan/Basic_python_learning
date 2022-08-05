# LIST []

# List are MUTABLE means ADD and REMOVE elements is possible


list1 = ['ADIL','RABBI',300,'RAIYAZ',500,'NOYON','SAKA']     # USE 'SQUARE BRACKET'

print(list1)            # print the list
print(list1[0])         # print the first item (list index value starts from '0' in a list) of the list
print(list1[2:])        # print everything from item3 (list index value '2') and onwards
print(500 in list1)     # check whether an item is listed, using 'in' or 'not in' operators (result will be in boolean expressions)
print('NOYON' not in list1)
print(list1 + [800])    # add new item into the last position of the list
print(list1*2)          # amplify the item's frequency of the list

# list 'index value' for the first entry of the list, 'ADIL' is equal to '0', 'RABBI' is equal to '1', '300' is equal to '2'....


# Nested Lists

list_a = [1, 43.5, ('Phoebe', 68), True]
list_b = ['apple', 'orange', 31]

nes_list = ['John', list_a, list_b, 'Denise']

print(nes_list)