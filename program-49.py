# Dictionaries
# a data structure of python, where the data are stored as value of a specific 'key'
# the value can only be accessed by the 'key'

studentID = {          # in dictionary use 'curly' bracket
    101 : 'Dhoni',     # 101 = key     # Dhoni = value
    102 : 'Yuvraj',
    103 : 'Shehwag'
}
# print(studentID[102])     # Use 'square' bracket

print(studentID.get(105,"Not a valid key"))