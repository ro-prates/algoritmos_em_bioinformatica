quantidade_cigarros = int(input('digite a quantidade de cigarros que voce fumou por dia:\n'))
quantidade_anos = int(input('por quanto tempo voce ja fumou? (em anos):\n'))

total_cigarros = quantidade_anos * 365 * quantidade_cigarros

resultado = total_cigarros * 10 / 1440

print(f'voce perdeu {resultado:.2f} de dias da sua vida.')