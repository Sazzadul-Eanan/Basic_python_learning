# Regular expression : Character classes []

# Character classes are sets of characters or ranges of characters enclosed by square brackets []



# Example - (1)

import re

patt = r'[aeiou]'                            # Means if there is any match in the beginning of the string for any of the substring from the list [aeiou]

if re.match(patt,'eghoklaeioumntpwi') :

    print ('Matched')
else :
    print('Not Matched')



# Example - (2)

import re

patt = r'[aeiou]'                             # Means if there is any match in the beginning of the string for any of the substring from the list [aeiou]

if re.match(patt,'geiouhghoklaeioumntpw') :

    print ('Matched')
else :
    print('Not Matched')







