# Public, Private & Portected #63

class Employee:
    no_of_leaves = 8
    var = 8
#       if im use one underscore [ _ ] its mean protect only use classes.
    _protect = 9
#       if im use two underscore [ __ ] its means private only use me.
    __private = 98

    def __init__(Self, aname, asalary, arole):

        Self.name = aname
        Self.role = arole
        Self.salary = asalary

    def printdetails(Self):
        return f"The Name is {Self.name}, Salary is {Self.salary}, and role is {Self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("rohan", 455, "Student")
karan = Employee.from_dash("karan-480-Studend")

#       if im use only private variabls, so use class name [_Employee] then type variabls name with underscore.
print(harry._Employee__private)
