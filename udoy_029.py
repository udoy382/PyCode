# if __name__ == "__main__": usage & necessity #46


def printhar(string):
    return f"Ye string udoy ko de de re ba ba {string}"

def add(num1, num2):
    return num1 + num2 +5

#       this function type here and run second file, to see run file name.
print("aand the name is", __name__)

#       if im use main function, not print in second file.
if __name__ == "__main__":
    print(printhar("Udoy1"))
    o = add(4, 6)
    print(o)
