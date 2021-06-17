import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axis import Axis

n = 500

x = np.random.rand(n)
y = np.random.rand(n)

fig, ax = plt.subplots()

for i in range(n):
    if x[i]**2 + y[i]**2 < 1:
        plt.plot(x[i], y[i], 'o', color='red')
    else:
      plt.plot(x[i], y[i], 'o', color='blue')

circle_plot = plt.Circle( ( 0, 0 ), 1, color='black', linewidth=5, fill=False)

Axis.set_zorder(circle_plot, 20)
ax.add_artist(circle_plot)

plt.title('Monte carlo calcula de pi 500 pts')
plt.xlabel('raio')
plt.ylabel('raio')
plt.grid()
plt.show()