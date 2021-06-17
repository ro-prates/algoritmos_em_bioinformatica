import numpy as np

n = int(input('digite a quantidade de números:\n'))

x = np.random.rand(n)
y = np.random.rand(n)

print(f'Valor aproximado de PI: {4 * np.sum(list(map(lambda x1, y1 : x1*x1 + y1*y1 < 1, x, y))) / n:.4f}')