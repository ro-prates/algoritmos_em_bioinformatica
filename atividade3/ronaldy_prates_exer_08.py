from math import pi, sin, cos, tan
import numpy as np
import matplotlib.pyplot as plt

intervalo = 4 * pi / 150

x = np.arange(-2*pi, 2*pi, intervalo)
y = np.sin(x)
z = np.cos(x)
w = np.tan(x)

'''
plt.plot(x, y, color='red')
plt.title('função seno(x)')
plt.show()

plt.bar(x, z)
plt.title('função cos(x)')
plt.show()
'''
plt.plot(x, w, 'o')
plt.title('função tg(x)')
plt.show()
