# Counting letters, digits and words from a text

numberOfdigits = 0
numberOfletters = 0
numberOfwords = 0

text = input('Enter a text of numbers :- ')

for i in text :

    i = i.lower()       # to convert the 'capital letter' as 'small letter'
    if i >= 'a' and i <= 'z' :
        numberOfletters = numberOfletters + 1

    elif i >= '0' and i <= '9' :
        numberOfdigits = numberOfdigits + 1

    elif i == ' ' :      # ' ' means the 'space' between two words
        numberOfwords = numberOfwords + 1

print('Letters : ',numberOfletters)
print('Digits : ',numberOfdigits)
print('Words : ',numberOfwords+1)   # number of words in a sentence is always '1' greater than the number of 'space' in between the words
