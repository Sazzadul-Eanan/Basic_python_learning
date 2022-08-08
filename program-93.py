# 00P : Object Oriented Programming

# Inside a CLASS there remain METHOD and OBJECT

# OBJECT is also known as INSTANCE


class student_details :                    # Creating a class                # 'Student_details' is the name of the class
    roll = ''
    gpa = ''
    standing = ''

Rahim = student_details()                  # Creating an object              # 'Rahim' is the name of the object
Rahim.roll = 1001
Rahim.gpa = 3.76
Rahim.standing = '2nd'
print (f'Roll : {Rahim.roll}, Gpa : {Rahim.gpa}, Standing : {Rahim.standing}')


Shafiq = student_details()                 # Another object
Shafiq.roll = 2002
Shafiq.gpa = 3.85
Shafiq.standing = '1st'
print (f'Roll : {Shafiq.roll}, Gpa : {Shafiq.gpa}, Standing : {Shafiq.standing}')



# To understand the f'' see program-13 again






