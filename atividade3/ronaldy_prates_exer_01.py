def fatorial(n):
    resultado = 1
    while n > 1:
        resultado *= n
        n -= 1
    return resultado

numero = int(input('digite um valor:\n'))
print(f'o fatorial de {numero} eh: {fatorial(numero)}')