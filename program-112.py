# Regular expression : Meta characters

# ^.....$ character

# Example - (1)

import re

patt = r'^American$'                      # Means the initial and the ending pattern needs to be exactly the same

if re.match(patt,'Americana') :           # 'Match()' gives output as boolean

    print ('Matched')
else :
    print('Not Matched')


# Example - (2)

import re

patt = r'^American$'

if re.match(patt,'American') :

    print ('Matched')
else :
    print('Not Matched')







