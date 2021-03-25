# Multiple Inheritance #61

class Employee:
    no_of_leaves = 8
    var = 8
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

class Flayer:
    no_of_games = 4
    var = 9
    def __init__(self, name, game):
        self.name = name
        self.game = game


    def printdetails(self):
        return f"The Name is {Self.name}, game is {Self.game}"

class Coolprogrammer( Flayer, Employee):
    # var = 10
    language = "c++"
    def printlanguage(self):
        print(self.language)

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("rohan", 455, "Student")

shubham = Flayer("Shubham", ["Cricket"])
karan = Coolprogrammer("Karan", ["Cricket"])

# det = karan.printdetails()
# karan.printlanguage()
# print(det)

print(karan.var)