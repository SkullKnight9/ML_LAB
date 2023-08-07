import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
x = np.arange(0,100)
#y = np.arange(0,200)
ax.plot(x,x*2)
plt.xlabel("x")
plt.ylabel("y")
plt.title("title")
plt.show()

