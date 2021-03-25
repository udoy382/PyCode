# Using With Block To Open Python Files #31

#       short write open or close file so using with function.
with open("udoy_1.txt") as f:
    a = f.read(4)
    print(a)
