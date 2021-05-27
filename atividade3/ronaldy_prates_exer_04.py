cadastro = dict()
lista = []

while True:
    cadastro.clear()
    cadastro['nome'] = input('digite o nome da pessoa:\n')
    cadastro['sexo'] = input('digite o sexo da pessoa:\n')
    cadastro['peso'] = float(input('digite o peso da pessoa:\n'))
    cadastro['altura'] = float(input('digite a altura da pessoa:\n'))

    lista.append(cadastro)

    continua = int(input('1- continuar\n2- encerrar\n'))
    if continua == 2:
        break

print(lista)

for i in lista:
    print(i['peso'])