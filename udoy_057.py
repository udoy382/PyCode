# Os Module #79

import os

#       see all command to using os module.
# print(dir(os))

#       see corrent directry.
# print(os.getcwd())

#       this command use for change directry.
# os.chdir("c://")
# print(os.getcwd())

#       if im change directry so cannot open this txt file.
# f = open("udoy_1.txt")

#       see all files on this directry.
# print(os.listdir("C://"))

#       see type on this list directry.
# print(type(os.listdir("C://")))

#       this commman use for make a folder.
# os.mkdir("This")

#       and this comman use for make a folder but wite ful command like [ makedires ].
# os.makedirs("This/that")

#       this comman use for change name any file.
# os.rename("srudoy_1.txt", "udoy_1.txt")

#       see all path on this comman
# print(os.environ.get("Path"))

#       this command use for  joine this txt file with c://.
# print(os.path.join("c://", "udoy_1.txt"))

#       get true or false if this path exist ture if this path cannot exist false.
# print(os.path.exists("C://Python"))
# print(os.path.isdir("C://Python"))