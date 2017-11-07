import numpy as np
#matplotlib is a huge library, only import pyplot, otherwise
#it'd be importing GB of library files each time u ran code
import matplotlib.pyplot as plt

# create x, evenly spaced between 0 and 20
# using linspace function of numpy
#gen 1000 numbers between
x = np.linspace(0, 20, 1000)
y1 = np.sin(x)
y2 = np.cos(x)

#plot the sin and cos functions -g = green
plt.plot(x , y1 , "-g", label="sine")
plt.plot(x , y2 , "-b", label="cos")

# the legend should be in the top right corner
plt.legend(loc = "upper right")

# Limit the y axis to -1.5 to 1.5
plt.ylim(-1.5, 1.5)
plt.show()
