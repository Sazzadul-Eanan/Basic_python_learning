# Regular expression : Meta characters

# Dot meta character

# Example - (1)

import re

patt = r'Banglad..h'                      # Means in the place of two dots there might be only any two characters

if re.match(patt,'Bangladesh') :          # 'Match()' gives output as boolean

    print ('Matched')
else :
    print('Not Matched')


# Example - (2)


import re

patt = r'Banglad.h'

if re.match(patt,'Bangladesh') :

    print ('Matched')
else :
    print('Not Matched')



