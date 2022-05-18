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
    def display_value(self) :
        print (f'Roll : {self.roll}, Gpa : {self.gpa}, Standing : {self.standing}')

                                                                   # Objects
rahim = student_details ()
rahim.input_value(101, 3.45, '3rd')
rahim.display_value()

himadri = student_details ()
himadri.input_value(201, 3.62, '2nd')
himadri.display_value()

phoebe = student_details ()
phoebe.input_value(301, 3.97, '1st')
phoebe.display_value()





