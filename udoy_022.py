# Recursions: Recursive Vs iterative Approach #34

# n! = n * n-1 * n-2 * n-3......1
# n! = n * (n-1)!

# recursive work method.
"""
5 * factroial_recursive(4)
5 * 4 * factroial_recursive(3)
5 * 4 * 3 * factroial_recursive(2)
5 * 4 * 3 * 2 * factroial_recursive(1)
5 * 4 * 3 * 2 * 1 = 120
"""

'''
def factroial_iterative(n):
    """
    :param n: Integer
    :return: n*n-1 * n-2 * n-3......1
    """
    fac = 1 
    for i in range(n):
        fac = fac * (i+1)
    return fac

def factroial_recursive(n):
    """
    :param n: Integer
    :return: n*n-1 * n-2 * n-3......1
    """
    if n==1:
        return 1
    else:
        return n * factroial_recursive(n-1)

number = int(input("Enter the number\n"))
print("Factorial Using Iterative Method:", factroial_iterative(number))
print("Factorial Using Recursive Method:", factroial_iterative(number))
'''
# Quiz...

# fibonacci: 0 1 1 2 3 5 8 13
"""
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
number = int(input("Enter the number\n"))
print(fibonacci(number))
"""