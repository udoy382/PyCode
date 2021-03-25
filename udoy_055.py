# Else & Finally In Try Except #76

f1 = open("udoy_1.txt")
try:
    f = open("does2.txt")

#       this is first way to print exept.
except Exception as e:
    print(e)

#       this is second way to print except.
# except EOFError as e:
#     print("Print eof error aa gaya hei", e)

#       this is third way to print except.
# except IOError as e:
#     print("print Io error aa giya hai", e)

#       run only one except or else any ones.
else:
    print("This will run only if except is not running")

#       finally is prined sure.
finally:
    print("Return ths anyway")

    f1.close()

print("Importent stuff")