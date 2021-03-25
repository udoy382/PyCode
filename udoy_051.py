# Generators In Python #72

"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration - 

"""
def gen(n):
    for i in range(n):
        yield i

g = gen(3)
print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# for i in g:
#     print(i)

u = "udoy"
ier = iter(u)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())

# for c in u:
#     print(c)