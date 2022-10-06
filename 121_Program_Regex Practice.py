# Regular Expression :

# Finding mobile number from a text

import re

text = "my house number is 123/a, my phone number is 01875137937"
match = re.search('\d{11}',text)              # \d+ means digits after digits
e = match.group()

print(e)

# But if we write the number in the form of 018 75137937 then the code will be (\d{3}\s*\d{8}
# In Regex \s means 'space', 'tab' or, 'newline'

# Finding only the mobile numbers from a text full of other spam numbers

tex = "here is some numbers : 01756 234567, 00000456783, 01967 121345, 098756235476, 999, 01875 137937, 87091234567"
result = re.findall(r'01[879]\d{2}\s*\d{6}',tex)

print(result)