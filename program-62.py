# Program for adding numbers using X-arguments

def add(*numbers) :
    sum = 0
    for x in numbers :
        sum = sum + x
    print(sum)

add(20, 30)
add(20, 20, 60)
add(50, 50, 50, 50)


