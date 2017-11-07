import numpy as np

x = [5,10,15,20,25]

# declare y as an empty list
y = []

#old fashined way below
for counter in x:
    y.append(counter / 5)

print("\nOld fashioned way: x = {} y = {} \n".format(x, y))

#new way using List comprehensions
#[ <do something> for value in list]

#divide x by 5
z = [n/5 for n in x] #[] convert to list
print("List Comprehensions: x = {} z = {} \n".format(x, z))

#below code will catch an exception
try:
    a = x / 5
except:
    print("No, you can't do that with regular Python lists\n")

#convert x to numpy array
a = np.array(x)
b = a / 5

print("With Numpy: a = {} b = {} \n".format(a, b))
