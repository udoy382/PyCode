# Scope, Global Variables and Keyword #33

"""
#       def outside function is Gobal Variables.
l = 10 #Global
def function1(n):
    # l = 5 #Local
    m = 8 #Local
    global l
    l = l + 45
    print(l, m)
    print(n, "I have printed")

function1("Hi i am udoy")
"""

"""
def udoy():
    x = 20
    def rohan():
        global x
        x = 88
    # print("befor calling rohan()", x)
    rohan()
    print("after calling rohan()", x)

udoy()
"""

# Quiz...
#       if im print [x] what value retrunes.
x = 89
def udoy():
    x = 20
    def rohan():
        global x
        x = 88
    # print("befor calling rohan()", x)
    rohan()
    print("after calling rohan()", x)

udoy()
print(x)