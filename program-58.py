# Dictionaries  { }

# a collection of item in python, where the data are stored as value of a specific 'key'
# the value can only be accessed by the 'key'
# MUTABLE and indexed
# the keys must be unique but the values do not need to be unique


studentID = {               # USE 'CURLY BRACKET'
    101 : 'Dhoni',          # 101 = key     # Dhoni = value
    102 : 'Yuvraj',
    103 : 'Shehwag'
}

print(studentID[102])               # return indexed value

print(len(studentID))               # return length

print(studentID.keys())             # return keys

print(studentID.values())           # return values

print(studentID.items())            # Return a list containing the tuple for each key-value pair

studentID.pop(102)                  # Remove the element with the specified key
print(studentID)


# Update the dictionary with a new key-value pair

anotherID = {
    104 : 'Sachin'
}
studentID.update(anotherID)
print(studentID)



# Creating a dictionary using dictionary function

dict1 = dict(uk='London', ireland='Dublin', france='Paris')
print('dict1:', dict1)


