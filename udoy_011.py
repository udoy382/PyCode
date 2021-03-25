# Break & Continue Statements In Python #18

# i = 0

# while(True):
#     if i+1<5:
#         i = i + 1
#         continue

#     print(i+1, end=" ")
#     if(i==44):
#         i = i + 1
#         break # stop the loop
#     i = i + 1

# Quiz...


while(True):
    x = int(input("Enter a number\n"))
    if x>=100:
        print("Congratuliton")
        break
    else:
        print("Try again")
        continue