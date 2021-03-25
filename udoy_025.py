# F-Strings & Sring Formatting In Python #39

import math

me = "Udoy"
a1 = 3

# This is 1st way to print or add.
"""
a = "This is %s %s"%(me, a1)
print(a)
"""
# This is 2nd way to print or add.
"""
a = "This is {1} {0}"
b = a.format(me, a1)
print(b)
"""
# This is f string to add 2 or more elemints easy.
a = f"This is {me} {a1} {math.cos(65)}"
print(a)