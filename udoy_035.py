# Instance & Class Variables #54

class Employee:
    no_of_leaves = 8
    pass


harry = Employee()
rohan = Employee()

harry.name = "harry"
harry.salary = 5550
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4500
rohan.role = "Student"

#       if im print Employee.no_of_leaves so print 8 cause its class function.
print(Employee.no_of_leaves)
#       thif function use for see all rool.
print(Employee.__dict__)
#       this function use for change class item. but we cannot change using other name without class name.
#       if im change class itployee.no_of_leaves = 9em so using class name not othes name.

print(Employee.__dict__)
print(Employee.no_of_leaves)