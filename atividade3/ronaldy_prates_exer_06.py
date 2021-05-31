import numpy as np

n = int(input('digite o tamanho do seu vetor:\n'))

# criando o vetor aleatório
vetor = np.random.randint(0, 1000, size = n)

print('valores da lista:')
print(vetor)

print('valores com o índice par:')
for i in range(0, len(vetor), 2):
    print(vetor[i])