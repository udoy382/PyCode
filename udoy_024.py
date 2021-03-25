# Using Python External & Built In Modules #38

#       import random module.
import random

#       this function use for any random number showes.
random_number = random.randint(0, 5)
# print(random_number)

#       this function use for randn number generet 0 t0 1 but if im give *100 or more number so generet this. 
rand = random.random() *100
# print(rand)

#       this function use for chose any name in list function.
lst = ["Star Plus", "DD1", "Aaj Tak", "Sony", "CN", "CodeWithHarry"]
choice = random.choice(lst)
# print(choice)