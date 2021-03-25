# Single Inheritance #60

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

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))


    @staticmethod
    def printgood(string):
        print("This is a good" + string)

#       we use this for using prebius class item in this class items.and add new items ans use older class item on this programm.
class Programmer(Employee):
    no_of_holyday = 56
    def __init__(self, aname, asalary, arole, alanguage):
        self.name = aname
        self.role = arole
        self.salary = asalary
        self.language = alanguage


    def printprog(self):
        return f"The Programmer Name is {self.name}, Salary is {self.salary}, and role is {self.role}. The language are {self.language}"


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("rohan", 455, "Student")

#       make a new variable name with items.
udoy = Programmer("Udoy", 345, "Programmer", ["Python"])
karan = Programmer("Karan", 555, "Programmer", ["Python", "c++"])

# print(karan.printprog())
# print(karan.printdetails())]
print(karan.no_of_holyday)
# print(udoy.printprog())