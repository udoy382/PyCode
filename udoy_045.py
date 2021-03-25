# Super() and Overriding In Classess #65

#       first make a class then set variabls.
class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.spacial = "Spacial"

#       if im make same class variabls so cannot print previous class variabls so used super function for print previous class.
class B(A):
    classvar1 = "I am class variable in class B"
    def __init__(self):

        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        super().__init__()
        print(super().classvar1)

a = A()
b = B()

print(b.spacial, b.var1, b.classvar1)