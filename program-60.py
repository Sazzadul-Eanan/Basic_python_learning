# X-arguments / Arbitrary arguments
# the way through which we can pass as many 'parameters' as we want within a 'function' without declaring any of the 'parameters'

def student (*details) :     # details is only a variable but the *(asterisks) play the role of the 'arguments'
    print(details)

student('Fahim')
student(1001, 'Fahim')
student(1001, 'Fahim', 'Male')
