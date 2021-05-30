# verificando se a quantidade é um valor inteiro e positivo
while True:
    try:
        n = int(input('informe quantas pessoas você deseja cadastrar:\n'))
        if n < 1:
            print('digite apenas valores positivos')
        else:
            break
    except ValueError:
        print('atenção!!! digite apenas números inteiros e não negativos')

# dicionário para salvar as pessoas individualmente
cadastro = dict()

# lista para armazenar todos os dicionários
lista = []

for i in range(n):
    # limpando o dicionário para salvar o próximo cadastro
    cadastro.clear()

    # salvando as informações das pessoas
    cadastro['nome'] = input('digite o nome da pessoa:\n')
    cadastro['sexo'] = input('digite o sexo da pessoa:\n')
    cadastro['peso'] = float(input('digite o peso da pessoa:\n'))
    cadastro['altura'] = float(input('digite a altura da pessoa:\n'))

    # salvando as informações no cadastro
    lista.append(cadastro)

print(f'quantidade de pessoas cadastradas: {n}')

# inicializando as variáveis
peso_medio = 0.0
altura_media = 0.0
imc = 0.0
imc_media = 0.0

# percorrendo toda a lista e fazendo as contas
for i in lista:
    peso_medio += i['peso']
    altura_media += i['altura']
    imc = i['peso'] / i['altura'] ** 2 
    imc_media += imc

peso_medio = peso_medio / n
altura_media = altura_media / n
imc_media = imc_media / n

print(f'peso médio: {peso_medio:.2f}')
print(f'altura média: {altura_media:.2f}')
print(f'IMC média: {imc_media:.2f}')