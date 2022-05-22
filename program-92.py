# Regular expression : Meta characters

# * (asterisk) character : 0 or, more



import re

patt = r'A*'                            # Means the character remains 0 times or more in the string

if re.match(patt,'American') :          # 'Match()' gives output as boolean

    print ('Matched')
else :
    print('Not Matched')



# Example - (2)

import re

patt = r'A*'

if re.match(patt,'morocco') :

    print ('Matched')
else :
    print('Not Matched')