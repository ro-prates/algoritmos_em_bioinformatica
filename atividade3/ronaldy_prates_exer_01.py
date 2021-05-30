# função que calcula o fatorial
def fatorial(n):
    resultado = 1
    while n > 1:
        resultado *= n
        n -= 1
    return resultado

valores = []

# lista para ter o controle dos valores que serão digitados
for i in range(1000):
    valores.append(str(i))

numero = input('digite um valor:\n')

# verificando se o valor digitado corresponde a restrição
while numero not in valores:
    numero = input('digite um valor inteiro entre 0 e 1000:\n')

# convertendo o valor para inteiro
numero = int(numero)

# exibindo resposta final
print(f'o fatorial de {numero} eh: {fatorial(numero)}')