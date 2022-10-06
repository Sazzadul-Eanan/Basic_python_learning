# Inheritance are of three types : Hierarchical, Multi-level and Multiple

# Now it's time for Multiple inheritance -

class A :
    def display (self) :
        print ('I am in class-A')

class B :
    def display (self) :
        print ('I am in class-B')

class C(A, B):
    pass                                      # 'pass' is a null operation and is useful when a statement is -
                                              # required syntactically but no code needs to be executed

Obj = C()
Obj.display()


# In Multiple inheritance if we inherit in the form of C(A, B) then the method of class-A will be prioritized and called
# But if we inherit in the form of C(B, A) then the method of class-B will be prioritized and called