# Regular Expression : sub()

# The 'sub()' can search an existing substring / pattern and replace it with a new one from the text

# 3 parameters can be passed within the function : sub (pattern_looking_for, pattern_replacement, pattern_from_the_text)



import re

pattern_searching = r'cricket'

text = 'My favourite game is cricket, I love to play cricket'

edited_text = re.sub(pattern_searching, 'football', text)

print(edited_text)


'''

# An additional parameter can be passed to replace a recurrent pattern for 'x' times

import re

pattern_searching = r'cricket'

text = 'My favourite game is cricket, I love to play cricket'

edited_text = re.sub(pattern_searching, 'football', text, count=1)        # Replace the pattern in its first count only  

print(edited_text)

'''