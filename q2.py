import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,.2,.2])
x = np.arange(0,100)
#y = np.arange(0,200)
ax1.plot(x,x*2)
ax1.set_title("Plot ax1")
ax2.plot(x,x*2)
ax2.set_title("Plot ax2")
plt.xlabel("x")
plt.ylabel("y")
#plt.title("title")
plt.show()