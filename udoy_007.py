# Sets in python #12

s = set()
# print(type(s))

#       make a set with list
# s_from_list = set([1, 2, 3, 4])
# print(s_from_list)
# # print(type(s_from_list))

#       add eliment in blank set, set needed unique values [ two 1 show one 1 ].
s.add(1)
s.add(2)
# s1 = s.union({1, 2, 3})
s1 = s.intersection({1, 2, 3})
# print(s, s1)

#       set function.
# print(len(s))
# print(max(s))
# print(min(s))
# print(type(s))
# s.remove(2)
# print(s)