# object Introspection #70


class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@srudoy.com"

    def emplain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set"
        return f"{self.fname}.{self.lname}@srudoy.com"

    @email.setter
    def email(self, string):
        print("Satting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

skillf = Employee("skill", "f")
# print(skillf.email)

#       thsi function show type in skillf or giving argiment.
# print(type(skillf))
# print(type("This is a string"))

#       this function show skillf or giving argiment id.
# print(id(skillf))
# print(id("That that"))

#       this function show all argiment to this skillf or giving statment.
# o = "This is a string"
# skillf = "This is a string"
# print(dir(skillf))

import inspect
print(inspect.getitemss(skillf))