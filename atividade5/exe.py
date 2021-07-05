# pontuação definida pelo exercício

gap = -2
mismatch = -1
match = 1

def smith_waterman(s1, s2):

    # tamanho das sequencias para a criação da matriz
    tamanho_s1 = len(s1)
    tamanho_s2 = len(s2)

    colunas = (tamanho_s1 + 1) #cols
    linhas = (tamanho_s2 + 1) #rows

    matriz = [[0] * colunas for i in range(linhas)]

    # direções para reconstruir o caminho de volta
    direcoes = {}

    for i in range(1, colunas):
    	direcoes[(0, i)] = (0, i - 1)
    for i in range(1, linhas):
    	direcoes[(i, 0)] = (i - 1, 0)

    # valor máximo, posição da linha, posição da coluna, respectivamente
    informacao_valor_maximo = [-1, -1, -1]

    # função que retonra o valor máximo
    def valor_maximo(i, j):

        resultado = 0
        if s2[i-1] == s1[j-1]:
            resultado = match
        else:
            resultado = mismatch

        valor1 = matriz[i-1][j-1] + resultado # diagonal da esquerda
        valor2 = matriz[i-1][j] + gap # topo
        valor3 = matriz[i][j-1] + gap # esquerda

        # calculando o valor máximo
        maximo_valor = max([0, valor1, valor2, valor3])

        # checando quem é o valor máximo e verificando o caminho a ser percorrido
        if maximo_valor == valor1:
            direcoes[(i, j)] = (i-1, j-1)
        elif maximo_valor == valor2:
            direcoes[(i, j)] = (i-1, j)
        else:
            direcoes[(i, j)] = (i, j-1)
        
        # verificando o maior valor da celula
        if informacao_valor_maximo[0] <= maximo_valor:
            informacao_valor_maximo[0] = maximo_valor
            informacao_valor_maximo[1] = i
            informacao_valor_maximo[2] = j
        return maximo_valor

    for i in range(1, linhas):
        for j in range(1, colunas):
            matriz[i][j] = valor_maximo(i, j)
    
    resultado_s1 = ''
    resultado_s2 = ''
    i = informacao_valor_maximo[1]
    j = informacao_valor_maximo[2]

    while True:
        i_proximo, j_proximo = direcoes[(i, j)]

        if (i-1) == i_proximo and (j-1) == j_proximo:
            resultado_s1 += s1[j_proximo]
            resultado_s2 += s2[i_proximo]
        elif (i-1) == i_proximo and j == j_proximo:
            resultado_s1 += '-'
            resultado_s2 += s2[i_proximo]
        elif i == i_proximo and (j-i) == j_proximo:
            resultado_s1 += s1[j_proximo]
            resultado_s2 += '-'

        i = i_proximo
        j = j_proximo

        if not matriz[i][j] or (not i and not j):
            break

    resultado_s1 = resultado_s1[::-1]
    resultado_s2 = resultado_s2[::-1]

    print(f'Sequência 1: {resultado_s1}')

    for i in range(linhas):
	    print(' '.join(str(i) for i in matriz[i]))

    return (resultado_s1, resultado_s2)

# sequencias s1 e s2

s1 = input('digite a sequencia S1:\n')
s2 = input('digite a sequencia S2:\n')

#s1 = 'CTAGTAAGAGTT'
#s2 = 'CTAAAGAAGTTA'