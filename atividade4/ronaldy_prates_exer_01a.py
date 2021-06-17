import numpy as np

n = int(input('digite a quantidade de números:\n'))

x = np.random.rand(n)
y = np.random.rand(n)

soma = 0 
dentro_circulo = 0

for i in range(n):
    soma = x[i]**2 + y[i]**2
    if soma < 1:
        dentro_circulo += 1

print(f'aproximação do valor de pi {4 * dentro_circulo / n:.2f}')

'''
import numpy as np
from random import random

def pi(n):
    return 4 * float(sum(1 if (random()**2 + random()**2) <= 1 else 0 for i in range(n)))/n

quantidade = int(input('digite a quantidade de números:\n'))

print(f'Aproximação do valor de pi: {pi(quantidade):.4f}')
'''