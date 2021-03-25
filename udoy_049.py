# Setters & Property Decorators #69


#       make a class function normaly.
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@srudoy.com"

    def emplain(self):
        return f"This employee is {self.fname} {self.lname}"

#       @property use for hide [ email() ] only print email not ().
#       and if im print email or change email name  so make a def function like this.
    @property
    def email(self):
        #   this function use for not show none none shows return value.
        if self.fname==None or self.lname == None:
            return "Email is not set"
        return f"{self.fname}.{self.lname}@srudoy.com"

#       this decoretors use for make a email. with setter function.
    @email.setter
    def email(self, string):
        print("Satting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

#       this decoretors use for deleted not deleted shows none.
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

udoy = Employee("Saifur Rahman", "Udoy")

# print(udoy.email)

#       this method to change email name.
udoy.fname = "US"
print(udoy.email)

udoy.email = "this.that@udoy.com"
print(udoy.email)

del udoy.email
print(udoy.email)