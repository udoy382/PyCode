# Multilevel  Inheritance #62

class Dad:
    basketball = 6

class Son(Dad):
    basketball = 9
    dance = 1
    def isdance(self):
        return f"Yes i dance {self.dance} no of times"

class Grandson(Son):
    dance = 6
    def isdance(self):
        return f"Jackson yeah! " \
            f"Yes i dance very awesomely {self.dance} no of time"


darry = Dad()
larry = Son()
harry = Grandson()

# print(harry.isdance())
print(harry.basketball)