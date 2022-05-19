# Constructor Method:

# Using this method the 'value' of an object can directly be input

# It reduces the necessity of calling the input function (here, constructor method)

class student_details :
    roll = ''
    gpa = ''
    standing = ''

    def __init__ (self, roll, gpa, standing) :                     # Constructor method
        self.roll = roll                                           # Use __init__ function
        self.gpa = gpa
        self.standing = standing

                                                                   # Output method
    def output_value(self) :
        print (f'Roll : {self.roll}, Gpa : {self.gpa}, Standing : {self.standing}')


rahim = student_details (1001, 3.65, '2nd')                # input value directly into the object name

rahim.output_value()                                       # calling the output method



himadri = student_details (2001, 3.82, '1st')

himadri.output_value()