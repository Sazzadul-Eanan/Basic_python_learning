# Queue.........'FIFO' (first in first out)

from collections import deque         # call a function for 'queue'

manline = deque(['Tushar', 'Pobel', 'Ridoy'])       # DOUBLE bracket for TWO different arguments of 'deque' and 'list'

print(manline)

manline.popleft()
print(manline)           # notice 'FIFO' in the output
