# X-arguments
# arguments give output as 'tuples' so from a 'multi-parameter' function every single items can be printed

def student (*details) :
    print(details[0])        # index value of expected output
'''
student('Fahim')
student(1001, 'Fahim')
'''
student(1001, 'Fahim', 'Male')


