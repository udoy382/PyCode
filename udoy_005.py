# Python Lists And List Functions #9

grocery = ["Harpic", "Vim bar", "Deodrant", "Bhindi", "Lollypop", 56]
# print(grocery[0])

numbers = [2, 7, 9, 11, 3]
# numbers = []
# print(numbers[2])

#       This function will change original list if im use this functrion.

# numbers.sort()
# numbers.reverse()
# print(numbers)

#       this function cannot change original list if im slicing.
#       when im slicing list, cannot use -2 , -3, etc only use [ ::-1 ]

# print(numbers[1:5:3])
# print(numbers)

#       list function.

# print(len(numbers))
# print(max(numbers))
# print(min(numbers))

# numbers.append(71)
# numbers.append(61)
# numbers.append(98)

# numbers.insert(2, 67)
# numbers.remove(9)
# numbers.pop()
# print(numbers)


#           Tuple.

# numbers[1] = 98
# print(numbers)

"""
Mutable - can change [list]
Immutable - cannot change [tuple]
"""

# tp = (1, 2, 3)
# tp = (1,) # use  koma [,] if one element in tuple
# tp[1] = 8 # cannot change tuple value

# print(tp)

a = 1
b = 8
"""
temp = a
a = b
b = temp
print(a, b)
"""
"""
a, b = b, a
print(a, b)
"""

# Search on google [python list function]