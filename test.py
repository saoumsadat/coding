import matplotlib.pyplot as plt
import numpy as np

x= np.array([15, 13, 18, 19, 14, 20, 10, 16, 14, 17, 13, 20])
y= np.array([77.624, 71.286, 87.129, 90.298, 74.455, 93.467, 61.781, 80.792, 74.455, 83.961, 71.286, 93.467])
print(x)
print(y)

plt.plot(x, y)
plt.title("Graph Name")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.xticks([8, 10, 12, 14, 16, 18, 20])
plt.yticks([60, 65, 70, 75, 80, 85, 90, 95])

plt.grid()
plt.show()