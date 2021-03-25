# Writing And Appending To A File #28

"""
#       open file write mode.
f = open("udoy_1.txt", "w")
#       if im write txt on .txt file so use this.
a = f.write("Udoy bhai bahut achhe hain\n")
print(a)

f.close()
"""

# f = open("udoy_1.txt", "w")
# a = f.write("Udoy bhai bahut achhe hain\n")
# print(a)
# f.close()

#       Handle read and write both.
f = open("udoy_1.txt", "r+")
print(f.read())
f.write("Thank You")