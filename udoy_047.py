# Operator Overloading & Dunder Methods #67

#       search on google [ Mapping Operators to Functions ].

class Employee:
    no_of_leaves = 8
    def __init__(Self, aname, asalary, arole):

        Self.name = aname
        Self.role = arole
        Self.salary = asalary

    def printdetails(Self):
        return f"The Name is {Self.name}, Salary is {Self.salary}, and role is {Self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

#       this is a operators overloading. to [ + ], [ - ], or more... search on google.
    def __add__(Self, other):
        return Self.salary + other.salary

    def __truediv__(Self, other):
        return Self.salary / other.salary

#       this is a dunder method.
    def __repr__(Self):
            return f"Employee ('{Self.name}', {Self.salary}, '{Self.role}')"

    def __str__(Self):
        return f"The Name is {Self.name}, Salary is {Self.salary}, and role is {Self.role}"


emp1 = Employee("Udoy", 456, "Programmer")
# emp2 = Employee("Rohan", 5, "Cleaner")
# print(emp1 / emp2)

#       if im print one dunder methon so easyly printed but
#       if im print one more dunder methon so print with name like [__str__], [__reper__].

print(str(emp1))