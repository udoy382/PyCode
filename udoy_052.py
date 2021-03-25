# Python Comprehensions #73 

#       this is first way to print list Comprehensions.
"""
ls = []
for i in range(100):
    if i%3==0:
        ls.append(i)

print(ls)
"""

#       this is second way to print list Comprehensions.
"""
ls = [i for i in range(100) if i%3==0]

print(ls)
"""

#       this way to print dict Comprehensions.
"""
# dict1 = {i:f"item{i}" for i in range(1000) if i%100==0}

dict1 = {i:f"item{i}" for i in range(5)}
dict2 = {value:key for key, value in dict1.items()}
print(dict1,"\n",dict2)
"""

#       this way to print set Comprehensions.
"""
dresses = {dress for dress in ["dress1", "dress2", "dress1", "dress2", "dress1", "dress2"]}
print(dresses)
print(type(dresses))
"""

#       this is wat to print generators Comprehensions.
"""
evens = (i for i in range(100) if i%2==0)
# print(type(evens))
# print(evens.__next__())

# for item in evens:
#     print(item)
"""