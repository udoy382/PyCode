# Open(), Read(), & Readline() For Reading File #26

#       open file using [f], then insert txt file name then insert momde.
f = open("udoy_1.txt", "rt")
#       redlines function use for all lines shows without newline like this [\n].
print(f.readlines())
#       redline function use for print one by one line.
# print(f.readline())
# print(f.readline())
# print(f.readline())
#       if im insert f.read(3), so print only 3 careture.
# content = f.read()

#       print like this, it is a true way to print line by line txt.
"""
for line in f:
    print(line, end="")
"""

# print(content)
#       same line can't print.
# content = f.read(36655)
# print("2", content)

#       if im open file so mustly close file
f.close()