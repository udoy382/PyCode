# Class Methods In Pythin #56


class Employee:
    no_of_leaves = 8
    def __init__(Self, aname, asalary, arole):

        Self.name = aname
        Self.role = arole
        Self.salary = asalary

    # def printdetails(Self):
    #     return f"The Name is {Self.name}, Salary is {Self.salary}, and role is {Self.role}"

#       @classmethod use for change class variable with using others name like harry , rohan.
    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("rohan", 455, "Student")

rohan.change_leaves(34)
print(rohan.no_of_leaves)