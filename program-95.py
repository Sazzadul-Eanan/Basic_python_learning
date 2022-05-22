# METHOD : A function used under a class is called method

# Using a common method (function) to print all the objects' output

class student_details :
    roll = ''
    gpa = ''
    merit = ''

                                        # creating the method
    def print_out (self) :
        print (f'Roll : {self.roll}, Gpa : {self.gpa}, Merit : {self.merit}')

rahim = student_details ()
rahim.roll = 123
rahim.gpa = 3.78
rahim.merit = '2nd'

rahim.print_out()                       # calling the function

himadri = student_details ()
himadri.roll = 546
himadri.gpa = 3.94
himadri.merit = '1st'

himadri.print_out()                     # calling the function




