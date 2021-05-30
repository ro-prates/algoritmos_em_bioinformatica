from math import pi

vetor = []

intervalo = 0

# inserindo os valores no vetor
for i in range(80):
    vetor.append(intervalo)
    intervalo += 8*pi/80

for i in vetor:
    print(f'{i:.2f}')