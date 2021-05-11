dna = input()

quantidadeA = dna.count("A")
quantidadeT = dna.count("T")
quantidadeG = dna.count("G")
quantidadeC = dna.count("C")

if quantidadeC + quantidadeA + quantidadeG + quantidadeT != len(dna):
    print('sequência de DNA inválida')
    exit
else:
    print('\nsequência digitada é válida')
    print(f'o número total de nucletídeos da sequência digitada é {len(dna)}')
    print('a sequência possui:')
    print(f'{quantidadeA} Adenina (A)')
    print(f'{quantidadeG} Guanina (G)')
    print(f'{quantidadeC} Citosina (C)')
    print(f'{quantidadeT} Timina (T)')
    print('A frequência de nucleotídeos na sequência é:')
    print(f'{quantidadeA/len(dna)*100:.2f}% Adenina (A)')
    print(f'{quantidadeG/len(dna)*100:.2f}% Guanina (G)')
    print(f'{quantidadeC/len(dna)*100:.2f}% Citosina (C)')
    print(f'{quantidadeT/len(dna)*100:.2f}% Timina (T)')