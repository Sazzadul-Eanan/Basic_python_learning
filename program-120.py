# Finding some words end with a specific substring in the end

import re

des = "afganistan, america, bangladesh, canada, denmark, england, greenland, iceland, netherlands, new zealand, sweden, switzerland"
lis = re.findall(r'(\w+lands*)',des)          # \w+ means one or, more letter and s* means 0 s or, 1 s
print(lis)

k = 'Bangladesh is our homeland'
match = re.search('B\w+h',k)                  # looking for bangladesh word
#match = re.search('B.+?h',k)
l = match.group()
print(l)

match = re.search('desh', 'bangladesh')       # re.search() has two arguments. the first one is what we are looking for ('desh'),
x = match.group()                             # and the second one is where to look for ('bangladesh')
print(x)

# Regex starts to look for something from the left-side of the string

s = 'Helsinki'
match = re.search('.',s)          # the dot symbol (.) means what ever the letter from the left
y = match.group()
print(y)

match = re.search('..',s)
z = match.group()
print(z)

match = re.search('H...i',s)
w = match.group()
print(w)

# Finding mobile number from a text

text = "my house number is 123/a, my phone number is 01875137937"
match = re.search('\d{11}',text)            # \d+ means digits after digits
e = match.group()
print(e)

# But if we write the number in the form of 018 75137937 then the code will be (\d{3}\s*\d{8}
# In Regex \s means 'space', 'tab' or, 'newline'

# Finding only the mobile numbers from a text full of other spam numbers

tex = "here is some numbers : 01756 234567, 00000456783, 01967 121345, 098756235476, 999, 01875 137937, 87091234567"
result = re.findall(r'01[879]\d{2}\s*\d{6}',tex)
print(result)

#

g = "banla, english, german"
u = re.findall(r'GERMAN', g, re.IGNORECASE)          # In short form use re.I
print(u)                                             # This is called flag