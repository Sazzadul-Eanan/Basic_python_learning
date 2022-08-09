# Regular expression : Meta characters

# ? (question) character : 0 or, 1 time maximum

# Example - (1)

import re

patt = r'ice(-)?cream'                    # Means the previous character remains 0 or, 1 time maximum in the string

if re.match(patt,'icecream') :

    print ('Matched')
else :
    print('Not Matched')


# Example - (2)

import re

patt = r'ice(-)?cream'

if re.match(patt,'ice--cream') :

    print ('Matched')
else :
    print('Not Matched')







