# Regular Expressions #86

import re

mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grossvenor Place
London SWIX 7HSc
phone: 44017-82299436
Fax: +8801782-299436
Email: tata@taiitaii.com
website: www.google.com
Directions: View maip
Tata Limited
Dr. David Landsman, executive director
18, Grossvenor Place
Londoon SWIXqq 7HSc
phoone: =44017822563699436
Fax: +440728763658793
Email: tata@tata222.com
website: www.facebook.com
Directions: View maiiiiiiiiiiiiiiiip'''

#       best function in this module.
# findall, search, split, sub, finditer
# print(r"\n")

# -------------------------
# Meta Charecter
# -------------------------

#       search on this mystr string.
"""
patt = re.compile(r'map')

mateches = patt.finditer(mystr)
for match in mateches:
    print(match)
    print(mystr[404:407])
"""
#       [ . ] any charecter (except newline charecter).
"""
patt = re.compile(r'.com')

mateches = patt.finditer(mystr)
for match in mateches:
    print(match)
"""
#       [ ^ ] starts with.
"""
patt = re.compile(r'^Tata')

mateches = patt.finditer(mystr)
for match in mateches:
    print(match)
"""
#       [ $ ] End with
"""
patt = re.compile(r'map$')

mateches = patt.finditer(mystr)
for match in mateches:
    print(match)
"""
#       [ * ] zero or more occurences, print all ai.
"""
# patt = re.compile(r'ai*')
# patt = re.compile(r'a*i*')
patt = re.compile(r'ai+')

mateches = patt.finditer(mystr)
for match in mateches:
    print(match)
"""
#       [ {} ] Excactly the specified number of occurrences.
"""
patt = re.compile(r'ai{2}')

mateches = patt.finditer(mystr)
for match in mateches:
    print(match)
"""
#       [ () ] capture a group.
"""
patt = re.compile(r'(ai){2}')

mateches = patt.finditer(mystr)
for match in mateches:
    print(match)
"""
#       [ | ] Either or.
"""
patt = re.compile(r'ai{1}|t')
patt = re.compile(r'ai{1}|Limited')

mateches = patt.finditer(mystr)
for match in mateches:
    print(match)
"""
# -----------------------
# Special Sequences
# -----------------------
"""
patt = re.compile(r'\ATata')
patt = re.compile(r'\bcom')
patt = re.compile(r'36\b')

mateches = patt.finditer(mystr)
for match in mateches:
    print(match)
"""
#       search only number in list.
"""
patt = re.compile(r'\d{5}-\d{4}')

mateches = patt.finditer(mystr)
for match in mateches:
    print(match)
"""