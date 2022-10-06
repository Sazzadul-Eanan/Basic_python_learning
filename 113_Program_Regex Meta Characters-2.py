# Regular expression : Meta characters

# ^.....$ character      ( ^ is called 'caret' symbol and $ is called 'dollar' symbol)

# Example - (1)

import re

patt = r'^American$'                      # Means the pattern within the INITIAL (^) to the END ($) needs to be exactly the same

if re.match(patt,'Americanos') :          # 'Match()' gives output as boolean

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







