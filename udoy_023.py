# Anonymous / Lambda Function In Python #36

#       this is lambda function.
# minus = lambda x, y: x-y

#       this is def function like lambda.
# def minus(x, y):
#     return x-y

#       if im print lamlba whos result showes, if im print def same result showes
#       lambda is a sort function.
# prit(minus(9, 4))

#       lambda sort function lambda and def.
# def a_first(a):
#     return a[1]

a = [[1, 14], [0, 6], [8, 23]]
a.sort(key=lambda x:x[1])
print(a)