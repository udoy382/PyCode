# Enumerate function #44

#       first make a list.
l1 = ["Bhindi", "Aloo", "Chopsticks", "Chowmein"]

#       this is first way to print, but not good way.
i = 1
for item in l1:
    if i%2 is not 0:
        print(f"Jarvis please buy {item}")
    i+=1

#       this is second way to print, good and easy way.
for index, item in enumerate(l1):
    if index%2==0:
        print(f"Jarvis please buy {item}")