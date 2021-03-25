# Static Methods In Python #58

class Employee:
    no_of_leaves = 8
    def __init__(Self, aname, asalary, arole):

        Self.name = aname
        Self.role = arole
        Self.salary = asalary

    def printdetails(Self):
        return f"The Name is {Self.name}, Salary is {Self.salary}, and role is {Self.role}"

#       @classmethod use for change class variable with using others name like harry , rohan.
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

#       this a static methods to print only argement.
"""
    @staticmethod
    def printgood(string):
        print("This is a good" + string)
"""

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("rohan", 455, "Student")
karan = Employee.from_dash("karan-480-Studend")

#       print static method print with name or class name.
# print(karan.printgood(" Udoy"))
Employee.printgood(" harry")
