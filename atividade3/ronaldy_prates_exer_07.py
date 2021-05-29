from numpy import random
import numpy as np
from math import sin

matrix = np.random.randint(-10, 65, size=(4, 5))

print('\nvalores aleatórios:\n')
print(matrix)
print('\nvalores absolutos:\n')
print(abs(matrix))

print('\nvalores dos senos:\n')
for i in matrix[0]:
    print(f'{sin(i):.2f}')

print('\nmaiores valores por coluna:\n')
maior = -11
for coluna in range(5):
    for linha in range(4):
        if maior < matrix[linha][coluna]:
            maior = matrix[linha][coluna]
    print(maior)
    maior = -11

print('\nsoma dos valores por coluna:\n')
soma = 0
for coluna in range(5):
    for linha in range(4):
        soma += matrix[linha][coluna]
    print(soma)
    soma = 0 

print('\nsoma dos valores por linha:\n')
soma = 0
for linha in range(4):
    for coluna in range(5):
        soma += matrix[linha][coluna]
    print(soma)
    soma = 0 

print('\nproduto dos valores por coluna:\n')
produto = 1
for coluna in range(5):
    for linha in range(4):
        produto *= matrix[linha][coluna]
    print(produto)
    produto = 1 