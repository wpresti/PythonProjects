import numpy as np
import matplotlib.pyplot as plt

#use fromfile for numbers
salary = np.fromfile("salaries.txt", dtype=int, sep=",")
#use genfromtxt for strings
names = np.genfromtxt("names.txt", dtype='str', delimiter=",")

x=np.arange(len(names))
plt.bar(x, salary)
# xticks - replace numbers in x with names
plt.xticks(x, names)
plt.ylabel("Salaries")
plt.xlabel("Names")
plt.title("Salary of 10 random people")
plt.show()

print(np.max(salary), np.min(salary), np.average(salary), np.median(salary))

#a[start value:end value] -- start or end could be blank to go up till or start at
#get rid of outliers that skew data

salaries_new = salary[2:-2]
names_new = names[2:-2]

x = range(len(names_new))
plt.bar(x, salaries_new)
plt.xticks(x, names_new)

plt.show()

print(np.max(salaries_new), np.min(salaries_new), np.average(salaries_new))
