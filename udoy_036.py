# Self & __init__() (Constructors) #55

class Employee:
    no_of_leaves = 8
    def __init__(Self, aname, asalary, arole):

        Self.name = aname
        Self.role = arole
        Self.salary = asalary

    # def printdetails(Self):
    #     return f"The Name is {Self.name}, Salary is {Self.salary}, and role is {Self.role}"

harry = Employee("Harry", 255, "Instructor")
# rohan = Employee()

"""
harry.name = "harry"
harry.salary = 5550
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4500
rohan.role = "Student"
"""

# print(rohan.printdetails())
# print(rohan.no_of_leaves)
# print(harry.printdetails())
print(harry.salary)
