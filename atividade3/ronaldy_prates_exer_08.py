from math import pi, sin, cos, tan
import numpy as np
import matplotlib.pyplot as plt

# definindo o intervalo
intervalo = 4 * pi / 150

# criando o vetor com os valores solicitados
x = np.arange(-2*pi, 2*pi, intervalo)
y = np.sin(x)
z = np.cos(x)
w = np.tan(x)

# plotando o gráfico do seno
plt.plot(x, y, color='red')
plt.title('função seno(x)')
plt.show()

# plotando o gráfico do cosseno
plt.bar(x, z)
plt.title('função cos(x)')
plt.show()

# plotando o gráfico da tangente
plt.plot(x, w, 'o')
plt.title('função tg(x)')
plt.show()