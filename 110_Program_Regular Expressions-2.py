# Regular Expression :

# Finding some words end with a specific substring in the end

import re

des = "afganistan, america, bangladesh, canada, denmark, england, greenland, iceland, netherlands, swazeland, sweden, switzerland"
lis = re.findall(r'(\w+lands*)',des)                 # \w+ means one or, more letter and s* means 0 s or, 1 s

print(lis)

# Use of Regex flag

g = "bangla, english, german"
u = re.findall(r'GERMAN', g, re.IGNORECASE)          # In short form use re.I
                                                     # This is called flag
print(u)

k = 'Bangladesh is our homeland'
match = re.search('B\w+h',k)                  # looking for 'Bangladesh' word
#match = re.search('B.+?h',k)
l = match.group()

print(l)

match = re.search('desh', 'bangladesh')       # re.search() has two arguments. the first one is what we are looking for ('desh'),
x = match.group()                             # and the second one is where to look for ('bangladesh')

print(x)


# Regex starts to look for something from the left-side of the string

s = 'Helsinki'
match = re.search('.',s)                      # the dot symbol (.) means what ever the first letter is from the left
y = match.group()

print(y)

match = re.search('..',s)
z = match.group()

print(z)

match = re.search('H...i',s)
w = match.group()

print(w)