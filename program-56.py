# Queue.........'FIFO'

from collections import deque

manline = deque(['Tushar', 'Pobel', 'Ridoy'])
# print(manline)

manline.popleft()
manline.popleft()
manline.popleft()

if not manline :
  print('No Person Left')
