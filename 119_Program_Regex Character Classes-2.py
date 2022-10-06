# Regular expression : Character classes []

# Character classes are sets of characters or ranges of characters enclosed by square brackets []

# Character class : Range


# Example - (1)

import re

patt = r'[a-z]'                          # Means if there is any match in the string for the range

if re.match(patt,'eghok') :

    print ('Matched')
else :
    print('Not Matched')



# Example - (2)

import re

patt = r'[0-9]'

if re.match(patt,'gioumtpw') :

    print ('Matched')
else :
    print('Not Matched')







