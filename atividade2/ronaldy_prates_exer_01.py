numero = int(input('digite um número:\n'))
razao = int(input('digite uma razão:\n'))

print('10 primeiros termos de sua PA:\n')
for i in range(10):
    print(numero, end=' ')
    numero += razao