tupla = (10, 4, 2, 7, 1)
maior = tupla[0]
maior_indice = 0
for i, valor in enumerate(tupla[1:]):
  if valor > maior:
    maior = valor
    maior_indice = i + 1

print(f"O maior valor está na posição {maior_indice}")
