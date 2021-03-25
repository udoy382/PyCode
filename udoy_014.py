# Functions And Docstrings #23

#       add two numbers with built in function.
# a = 9
# b = 8
# c = sum((a,b)) # built in function

#       this is a def function, print this massage and add two numbers, 
#       if im use print statment returen none use only like this[function(5, 7)].
# def function1 (a, b):
#     print("Hello you are in function 1", a+b)
# print(function1(5, 7))
# function1(5, 7)

#       this function will add two numbers, and use doc string under first line in def function.
def function2(a, b):
    """This is  a function which will calculate average of two numbers,
    this function doesnt work for three numbers"""
    average = (a+b)/2
    # print(average)
    return average

# v = function2(5, 7)
# print(v)

#       this function will print docstring.
print(function2.__doc__)

# search on google [def functions in python]