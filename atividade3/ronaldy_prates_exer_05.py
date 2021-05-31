import numpy as np
from math import pi

# criando o vetor que foi solicitado
vetor = np.linspace(0, 8*pi, 80)

for i in vetor:
    print(f'{i:.2f}')