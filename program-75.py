# 00P : Object Oriented Programming

# Inside a class there remain the object

# Object is also known as instance


class student_details :                    # Creating class              # 'Student_details' is the name of the class
    roll = ''
    gpa = ''


Rahim = student_details()                  # Creating object             # 'Rahim' is the name of the object
Rahim.roll = 1001
Rahim.gpa = 3.76
print (f'Roll : {Rahim.roll}, Gpa : {Rahim.gpa}')

Shafiq = student_details()                 # Another object
Shafiq.roll = 2002
Shafiq.gpa = 3.85
print (f'Roll : {Shafiq.roll}, Gpa : {Shafiq.gpa}')


# To understand the f'' see program-12 again





