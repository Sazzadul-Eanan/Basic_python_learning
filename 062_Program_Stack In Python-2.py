# Stack......'LIFO'

books = []

books.append('Read')
books.append('Write')
books.append('Speak')
books.append('Listen')

print(books)
print('Stacking is done.')

books.pop()         # 1st pop
print(books)

print('After the first pop, right now the top book is : ', books[-1])
