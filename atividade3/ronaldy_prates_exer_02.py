# função que retorna o maior valor de um conjunto, utilizando empacotamento
def maxnum(*valores):
    maior = -99999
    for i in valores:
        if i > maior:
            maior = i
    return maior

# conjunto para testes, mas esses valores também poderiam ser digitados
resultado = maxnum(122, 298, 300, 431, 225, 86, -787, 80)

# exibindo resposta final
print(f'o maior valor do meu conjunto de elementos eh: {resultado}')