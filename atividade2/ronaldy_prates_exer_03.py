valor = 1

for i in range(5):
    for j in range(i+1):
        print(valor, end=' ')
        valor += i+1
    valor = i+2
    print()