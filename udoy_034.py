# Creating Our First Class In Python #53


class Student:
    pass

harry = Student()
larry = Student()

harry.name = "Harry"
harry.std = 12
harry.section = 1
larry.std = 9
larry.subject = ["Hindi", "physics"]

print(harry.std, larry.subject)