arquivo = open('Corona_genomic.fasta', 'r')
linhas = arquivo.readlines()

linhas_importantes = []

for linha in linhas:
    if linha.find('>') != 0: # vai ignorar as linhas que não são importantes
        linhas_importantes.append(linha)

print(linhas_importantes)