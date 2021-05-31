# função que verifica se os números são múltiplos 
def multiplo(primeiro, segundo):
    if segundo != 0:
        if primeiro % segundo == 0:
            return True
    return False

# verificando se os números são inteiros
while True:
    try:
        m = int(input('digite o primeiro valor:\n'))
        break
    except ValueError:
        print('atenção!!! digite apenas números inteiros')

# verificando se os números são inteiros
while True:
    try:
        n = int(input('digite o segundo valor:\n'))
        break
    except ValueError:
        print('atenção!!! digite apenas números inteiros')

# exibindo resposta final
print(multiplo(m, n))