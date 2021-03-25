# Python exercise2 #15

print("Enter first number")
num1 = int(input())
print("Enter second number")
num2 = int(input())
print("Enter operator")
op = input()

if op=='+' and num1==56 and num2==9:
    print("77")
elif op=='-' and num1==65 and num2==5:
    print("60")
elif op=='*' and num1==45 and num2==3:
    print("555")
elif op=='/' and num1==56 and num2==6:
    print("4")
elif op=='+':
    print(num1+num2)
elif op=='-':
    print(num1-num2)
elif op=='*':
    print(num1*num2)
elif op=='/':
    print(num1/num2)
else:
    print("Invalid Syntex")