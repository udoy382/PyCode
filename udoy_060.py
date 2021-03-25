# Pickle Module #84

import pickle

#       Pickling python object making 1st step then comment this.
# cars = ["Audi", "BMW", "Maruti Suzuki", "Harryti Tuzuki"]

# file = "mycar.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(cars, fileobj)
# fileobj.close()

#       making pickle decode using this program.
file = "mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))
