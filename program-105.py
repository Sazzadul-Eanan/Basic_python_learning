# Polymorphism : when a function has different types of usability depending on its use then this is called polymorphism of that fuction

# Polymorphic function is of two kind : built-in polymorphic function and user-defined polymorphic function



# A Built-in polymorphic function -

print(len('Sazzadul Eanan'))      # Here the polymorphism of the function 'len' is calculating the length of both a string and a list of numbers
print(len([20, 30, 40, 50]))




# An User-defined polymorphic function -

def add (x, y, z = 0) :
    return x + y + z

print(add(200, 300))             # Here the polymorphism of the function is its usability for adding two numbers and again adding three numbers
print(add(200, 300, 400))
