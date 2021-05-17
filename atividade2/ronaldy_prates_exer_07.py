arquivo = open('seq_a.fasta', 'r')
linhas = arquivo.readlines()
arquivo.close()

sequenciaA = []

for linha in linhas:
    if linha.find('>') != 0: # vai ignorar as linhas que não são importantes
        sequenciaA.append(linha)

arquivo = open('seq_b.fasta', 'r')
linhas = arquivo.readlines()
arquivo.close()

sequenciaB = []

for linha in linhas:
    if linha.find('>') != 0: # vai ignorar as linhas que não são importantes
        sequenciaB.append(linha)
         
contador = 0
trocas = 0

for linha in range(5):
    for coluna in range(60):
        contador += 1
        if contador > 200:
            break
        if sequenciaA[linha][coluna] != sequenciaB[linha][coluna]:
            trocas += 1
            print(f'a posição {contador} foi trocado {sequenciaA[linha][coluna]} --> {sequenciaB[linha][coluna]}')

print(f'o número de nucleotídeos diferentes é {trocas}')