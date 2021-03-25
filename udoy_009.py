# For Loops In Python #16

#       make a list of list
list1 = [ ["Harry", 1],  ["Larry", 2], ["Carry", 6], ["Marie", 200] ]

#       this way to print all item in list
# print(list1[0], list1[1])

#       conbard list to dict
dict1 = dict(list1)
# print(dict1)

#       only key prints 
# for item in dict1:
#     print(item)

#       this way to print all items in list or tupple
# for item, lollypop in dict1.items():
#     print(item, "and lolly is", lollypop)


# Quiz...

items = [int, float, "Udoy", 2, 5, 67, 8, 9, 90, 576 ,43, 6, 3]

#       int and float is not a isnumeric so typecust item in to str
for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)