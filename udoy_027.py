# Time Module In Python #42

#       see how much time run in For and While loops.
"""
import time
initial = time.time()
# print(initial)
k = 0
while(k<45):
    print("This is udoy bhai")
#       this is time.sleep function to sleep 2 secod.
    time.sleep(2)
    k+=1
print("While loop ran in", time.time() - initial, "Second")

initial2 = time.time()
for i in range(45):
    print("This is Udoy bhia")
print("For loop ran in", time.time() - initial2, "Second")
"""

#       see local time.
"""
localtime = time.asctime(time.localtime(time.time()))
print(localtime)
"""