# METHOD : A function used under a class is called method

# Using a common method (function) to input and output all the objects

class student_details :
    roll = ''
    gpa = ''
    standing = ''

    def input_value (self, roll, gpa, standing) :                  # Input method
        self.roll = roll
        self.gpa = gpa
        self.standing = standing

                                                                   # Output method
    def output_value(self) :
        print (f'Roll : {self.roll}, Gpa : {self.gpa}, Standing : {self.standing}')

                                                       # Creating an object
rahim = student_details ()

rahim.input_value(101, 3.45, '3rd')                    # Calling input method

rahim.output_value()                                   # calling output method


himadri = student_details ()

himadri.input_value(201, 3.62, '2nd')

himadri.output_value()


phoebe = student_details ()

phoebe.input_value(301, 3.97, '1st')

phoebe.output_value()





