# Join Function In Python #47

lis = ["John", "Cena", "Randy", "Orton", "Sheamus", "Khali", "Jinder mahal"]

#       this way to print [ and ] in item.
# for item in lis:
#     print(item, "and", end=" ")
# print("Other wwe superstars")

#       this is join function to add  [ and ] in itme.
a = " , ".join(lis)
print(a, "Other wwe superstars")