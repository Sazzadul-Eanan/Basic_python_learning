# Regular Expressions (regex) are used to match and extract any string related pattern from the strings of text such as particular word, or patterns of character

# Regex are tools for processing and manipulating text or, strings

# The most common use of regex is FORM VALIDATION, i.e. email validation, password validation, phone number validation etc.

# Some most used functions of 're' (Regex) module are - match(), search(), findall()



# Use 'match()' to check the match at the beginning of a string
# This function gives output in boolean

import re                    # importing the 're' module

pattern = r'colour'          # r' ' means that the string is to be treated as a RAW STRING, which means all escape codes will be ignored

if re.match(pattern, 'Red is the colour from my favourite colour') :
    print('Matched')

else :
    print('Not Matched')



# Use 'findall()' to get a list of all substrings that match a pattern

import re

pattern = r'colour'

w = re.findall(pattern, 'Red is the colour from my favourite colour')

print(w)



# Use 'search()' to find a match of a pattern anywhere in the string
# This function gives output in boolean

import re

pattern = r'my'

if re.search(pattern, 'Red is the colour from my favourite colour') :
    print('Matched')

else :
    print('Not Matched')


'''

# 'search()' can also generate the index values of a specific substring from both end

import re

sub_string = r'colo'

text = 'My favourite colour is red colour'

y = re.search(sub_string, text)

if y :                                            # if any value for 'y' is found then print 
    print(y.start())
    print(y.end())
    print(y.span())

'''





