# Seek(), tell() & More On Python Files #30

#       open file.
f = open("udoy_1.txt")
#       tell function use for see where mouse pointer in text.
print(f.tell())
print(f.readline())
# print(f.tell())
#       seek function use for where to start next line.
f.seek(10)
print(f.readline())
# print(f.tell())

f.close()