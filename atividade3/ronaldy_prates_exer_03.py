def multiplo(primeiro, segundo):
    if primeiro % segundo == 0:
        return True
    return False

m = int(input('digite o primeiro valor:\n'))
n = int(input('digite o segundo valor:\n'))

print(multiplo(m, n))