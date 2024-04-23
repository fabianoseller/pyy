tupla = (1, 2, 3, 4, 5)
valor_procurado = 3

valor_encontrado = False
for valor in tupla:
  if valor == valor_procurado:
    valor_encontrado = True
    break

if valor_encontrado:
  print(f"O valor {valor_procurado} está presente na tupla")
else:
  print(f"O valor {valor_procurado} não está presente na tupla")
