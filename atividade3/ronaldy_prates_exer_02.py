def maxnum(*valores):
    maior = -99999
    for i in valores:
        if i > maior:
            maior = i
    return maior

resultado = maxnum(122, 298, 300, 431, 225, 86, -787, 80)

print(f'o maior valor do meu conjunto de elementos eh: {resultado}')