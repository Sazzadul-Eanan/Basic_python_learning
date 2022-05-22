# Stack......'LIFO' (Last in first out)

books = []

books.append('Read')      # push item into the stack
books.append('Write')
books.append('Speak')
print(books)
print('Pushing items into the stack is done.')


books.pop()               # remove item from the stack
print(books)              # notice the LIFO action into the 'output'
