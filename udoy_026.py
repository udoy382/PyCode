# *args and **kwargs In Python #41

#       add item not good way.
# def function_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)

#       first make a def function for use *args and **kwargs.
def funargs(normal, *args, **kwargs):
    print(normal)
    # print(type(args)) # args need tupple.
    # print(type(kwargs)) # kwargs need dict.
    # print(args[0])
#       run loop for print all items.
    for itme in args:
        print(itme)
    print("\nNow I would like to interoduce some of our herose")
    for key, value in kwargs.items():
        print(f"{key} Like {value}")

# function_name_print("Udoy", "Harry", "Rohan", "Mahi", "Hammad")

har = {"Udoy", "Harry", "Rohan", "skillf", "hammad", "shivam", "Fariha"}

normal = "Im a normal agrimant and the student are"
kw = {"Udoy":"Lollypop", "Mahi":"Burger", "Mariyam":"Apple", "Fariha":"Pizza", "Mitu":"Rice", "Hammad":"Fish"}
#       call in function.
funargs(normal, *har, **kw)