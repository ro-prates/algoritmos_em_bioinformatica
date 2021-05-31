from math import pi, sin, cos, tan
import numpy as np
from matplotlib import pyplot as plt

# definindo o intervalo
intervalo = 4 * pi / 150

# criando o vetor com os valores solicitados
x = np.arange(-2*pi, 2*pi, intervalo)
y = np.sin(x)
z = np.cos(x)
w = np.tan(x)

figura = plt.figure(figsize=(7, 7))

# plotando o gráfico do seno
seno = figura.add_subplot(2, 2, 1)
seno.plot(x, y, color='red')
plt.title('função seno(x)')

# plotando o gráfico do cosseno
cosseno = figura.add_subplot(2, 2, 2)
cosseno.bar(x, z)
plt.title('função cos(x)')

# plotando o gráfico da tangente
tangente = figura.add_subplot(2, 2, 3)
tangente.plot(x, w, 'o')
plt.title('função tg(x)')