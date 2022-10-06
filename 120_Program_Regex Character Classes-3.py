# Regular expression : Character classes []

# Character classes are sets of characters or ranges of characters enclosed by square brackets []

# Character class : Multiple Range


# Example - (1)

import re

patt = r'[A-Z][a-z][0-9]'                    # In case of multiple range match checking the string should have the same order of the ranges

if re.match(patt,'567eghoASDO') :

    print ('Matched')
else :
    print('Not Matched')



# Example - (2)

import re

patt = r'[A-Z][a-z][0-9]'

if re.match(patt,'Ar9') :

    print ('Matched')
else :
    print('Not Matched')







