largura = float(input('digite a largura da parede (em metros):\n'))
altura = float(input('digite a altura da parede (em metros):\n'))

area = largura * altura
quantidade_tinta = area / 3

print(f'\narea: {area}m²'
      f'\nquantidade de tinta: {quantidade_tinta:.2f}litros')