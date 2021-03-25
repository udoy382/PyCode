# Raise In PYthon + Examples #89

#       this is our raise Exception method to show error in programmer dont print all lines.
"""
a = input("What is your name: ")
b = input("How much do you earn")

if int(b)==0:
    raise ZeroDivisionError("B is 0 so stoping the program")
if a.isnumeric():
    raise Exception("Numbers are not allowed")
print(f"Hello {a}")

    # 1000 lines taking 1 hour
"""

# Task - Wite about 2 built in Exception.

c = input("Enter your name: ")
try:
    print(a)
except Exception as e:
    if c=="Udoy":
        raise ValueError("Udoy is blocked he is not allowed")
    print("Exception handled")