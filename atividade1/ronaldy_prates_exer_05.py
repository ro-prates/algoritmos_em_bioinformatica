dias = int(input('digite a quantidade de dias:\n'))
horas = int(input('digite a quantidade de horas:\n'))
minutos = int(input('digite a quantidade de minutos:\n'))
segundos = int(input('digite a quantidade de segundos:\n'))

resultado = dias * 86400 + horas * 3600 + minutos * 60 + segundos

print(f'resultado: {resultado} segundos')