# Regular expression : Meta characters

# + (plus) character : 1 or, more

# Example - (1)

import re

patt = r'A+'                          # Means the character remains 1 time or more in the string

if re.match(patt,'Chinese') :

    print ('Matched')
else :
    print('Not Matched')


# Example - (2)

import re

patt = r'A+'

if re.match(patt,'Arctic') :

    print ('Matched')
else :
    print('Not Matched')







