arquivo = open('Corona_genomic.fasta', 'r')
linhas = arquivo.readlines()
arquivo.close()

linhas_importantes = []

for linha in linhas:
    if linha.find('>') != 0: # vai ignorar as linhas que não são importantes
        linhas_importantes.append(linha)

novo1 = []
teste = ''

for i in linhas_importantes:
    insere = i.replace('T', 'X')
    teste = teste+insere 
novo1.append(teste)

novo2 = []
teste = ''

for i in novo1:
    insere = i.replace('A', 'T')
    teste = teste+insere 
novo2.append(teste)

novo3 = []
teste = ''

for i in novo2:
    insere = i.replace('X', 'A')
    teste = teste+insere 
novo3.append(teste)

novo4 = []
teste = ''

for i in novo3:
    insere = i.replace('G', 'Y')
    teste = teste+insere 
novo4.append(teste)

novo5 = []
teste = ''

for i in novo4:
    insere = i.replace('C', 'G')
    teste = teste+insere 
novo5.append(teste)

complementar = []
teste = ''

for i in novo5:
    insere = i.replace('Y', 'C')
    teste = teste+insere 
complementar.append(teste)
print(complementar)

salvando = open('ex07_a.txt', 'w')
salvando.writelines(complementar)

salvando.close()