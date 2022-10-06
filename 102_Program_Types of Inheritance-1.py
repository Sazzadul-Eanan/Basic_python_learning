# Inheritance are of three types : Hierarchical, Multi-level and Multiple

# So far we have seen (in the previous) hierarchical inheritance

# Now it's time for Multi-level inheritance - when class-A inherits by class-B and class-B inherits by class-C.......

class A :                                       # class-A
    def display_1 (self) :
        print ('I am in class-A')

class B(A):                                     # class-B inherits class-A
    def display_2 (self) :
        print ('I am in class-B')

class C(B):                                     # class-C inherits class-A and class-B
    def display_3 (self) :
        print ('I am in class-C')


Obj = C()                                       # have created object for only 'class-c' but -
                                                # due to multilevel inheritance all three methods can be accessed
Obj.display_1()
Obj.display_2()
Obj.display_3()




'''

# To reduce all three individual call for three different method 

class C(B): 
    def display_3 (self) :
    
        super().display_1()
        super().display_2()
        
        print ('I am in class-C')
        
        
Obj = C()
Obj.display_3()
        
'''