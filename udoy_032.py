# Decorators In Python #51

#       if im store function in varaibal then use del function for deleted function, 
#       not deleted function cause we store function in variable.

# def function1():
#     print("Subscribe now")

# func2 = function1
# del function1
# func2()

#       print and sum also a function.
# def funcret (num):
#     if num==0:
#         return print
#     if num==1:
#         return sum

# a = funcret(1)
# print(a)



# def executor (func):
#     func("this")

# executor(print)

#       this is owr decorators.
def dec1 (func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec

# @dec1 # use this same print.
def who_is_harry():
    print("Harry is a good boy")

who_is_harry = dec1(who_is_harry) # or use this same print.
who_is_harry()