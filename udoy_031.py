# Map, Filter & Reduce #48 

#       this is simple program to type cust str to int the add number.
# numbers = ["3", "34", "64"]

# for i in range (len(numbers)):
#     numbers[i] = int(numbers[i])

# numbers[2] = numbers[2] + 1
# print(numbers[2])

#       this is map function first type cust str to int then add number.
numbers = ["3", "34", "64"]
numbers = list(map(int, numbers))

# numbers[2] = numbers[2] + 1
# # print(numbers[2])

#       this functio use for retuen square.
# def sq(a):
#     return a*a
# num = [2, 4, 7, 5, 9, 23, 33, 55, 67, 43, 77, 89]
# square = list(map(sq, num))
# print(square)

#       this is previous function work same but there using lambda function.
# num = [2, 4, 7, 5, 9, 23, 33, 55, 67, 43, 77, 89]
# square = list(map(lambda x:x*x, num))
# print(square)

#       this is our map function.
# def square(a):
#     return a*a

# def cub(a):
#     return a*a*a

# func = [square, cub]
# # num = [2, 4, 7, 5, 9, 23, 33, 55, 67, 43, 77, 89] #not used this line.
# for i in range(5):
#     val = list(map(lambda x:x(i), func))
#     print(val)


#       this is our filter function.
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def is_greater_5(num):
#     return num>5

# gr_than_5 = list(filter(is_greater_5, list1))
# print(gr_than_5)

#       this is reduce function to a sum all numbers in list.
from functools import reduce

list1 = [1, 2, 3, 4, 2]
num = reduce(lambda x,y: x*y, list1)
# num = 0
# for i in list1:
#     num = num + i
print(num)