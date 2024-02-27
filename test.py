import matplotlib.pyplot as plt
import numpy as np

x= np.arange(5)
y= np.array([0, 2, 4, 6, 8])
print(x)
print(y)

plt.plot(x, y)
plt.title("Graph Name")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.xticks([0,1,2,3,4])
plt.yticks([0,2,4,6,8])

plt.grid()
plt.show()