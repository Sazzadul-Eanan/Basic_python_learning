# Regular expression : Meta characters

# {and} character : 'x' to 'y' time

# Example - (1)

import re

patt = r'a{1,3}$'                        # Means that only this character (no other character) remains 'x' minimum times to 'y' maximum number of times in the whole string

if re.match(patt,'aa') :

    print ('Matched')
else :
    print('Not Matched')



# Example - (2)

import re

patt = r'd{1,2}$'                         # Don't forget to put an end sign ($) at the end

if re.match(patt,'ddd') :

    print ('Matched')
else :
    print('Not Matched')







