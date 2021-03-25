# Json Module #82

import json

data = '{"var1":"Harry", "var2":56}'
# print(data)

# print(type(data))

paresed = json.loads(data)
# print(paresed['var1'])
# print(type(paresed))

data2 = {
    "channel_name": "CodeWithHarry",
    "cars":['bmw', 'audi a8', 'ferrari'],
    "fridge":('roti', 540),
    "isbad":False
}
# jscomp = json.dumps(data2)
# print(jscomp)