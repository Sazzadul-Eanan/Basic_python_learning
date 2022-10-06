# Exception Handling

# Exception Handling (TypeError) of A User-defined Function While Performing Division

def divide (x, y) :
    try :
        return x / y
    except TypeError :
        print('Unsupported type. Did you use string ?')

print (divide(10, 2))
print (divide(9, 3))
print(divide('20', 5))           # 3RD call
print (divide(39, 3))


# In this program we input STRING in term of INTEGER for the 3RD call which is a 'TypeError'