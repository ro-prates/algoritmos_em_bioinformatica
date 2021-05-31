import numpy as np
from matplotlib import pyplot as plt
import math

import math

x= np.arange(-2*math.pi,2*math.pi,4*math.pi/150) #vetor com 150 pontos linearmente espaçados entre -2pi e 2pi.

fig = plt.figure(figsize=(10, 10))

#gráfico seno
y1= np.sin(x) 
ax1 = fig.add_subplot(2,2,1)
ax1.plot(x,y1,'r',linewidth=2)
plt.title('função seno(x)')

#gráfico cosseno
y2=np.cos(x)
ax2 = fig.add_subplot(2,2,2)
plt.bar(x,y2)
plt.title('função cos(x)')

#gráfico tangente
y3=np.tan(x)
ax2 = fig.add_subplot(2,2,3)
ax2.plot(x,y3,'bo')
plt.ylabel('valor de tg(x)')
plt.xlabel('valor de x')
plt.title('função tg(x)')