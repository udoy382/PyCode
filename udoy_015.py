# Try Except Exception Handling In Python #24

print("Enter num 1")
num1 = input()
print("Enter num 2")
num2 = input()
try:
    print("The sum of these two numbers is", int(num1) + int(num2))
except Exception as e:
    print("SORRY", e)

print("This line is very important")