tupla = (10, 4, 2, 7, 1)
menor = tupla[0]
menor_indice = 0
for i, valor in enumerate(tupla[1:]):
  if valor < menor:
    menor = valor
    menor_indice = i + 1

print(f"O menor valor está na posição {menor_indice}")
