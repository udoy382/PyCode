# Diamond Shape Problem In Multiple Inheritance #66

class A:
    def met(self):
        print("This is a mathod from class A")

class B(A):
        def met(self):
            print("This is a mathod from class B")


class C(A):
        def met(self):
            print("This is a mathod from class C")


class D(C, B):
        def met(self):
            print("This is a mathod from class D")


a = A()
b = B()
c = C()
d = D()

D.met(())