deposito_inicial = float(input('digite o valor do deposito inicial:\n'))
taxa_juros = float(input('digite o valor da taxa de juros:\n'))
controle = deposito_inicial

for i in range(24):
    deposito_inicial += deposito_inicial * taxa_juros / 100
    print(f'Mês {1+i}: R${deposito_inicial:.2f}')

print(f'\ntotal ganho: R${deposito_inicial-controle:.2f}')