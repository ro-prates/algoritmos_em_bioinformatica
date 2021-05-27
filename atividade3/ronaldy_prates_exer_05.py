from math import pi

vetor = []

intervalo = 0

for i in range(80):
    vetor.append(intervalo)
    intervalo += 8*pi/80

print(vetor)