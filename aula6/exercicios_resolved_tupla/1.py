#1. Encontrar o maior valor em uma tupla:
#Modifique o código para encontrar o maior valor em vez do menor.
tupla = (10, 4, 2, 7, 1)
maior = tupla[0]
for valor in tupla[1:]:
  if valor > maior:
    maior = valor

print(f"O maior valor na tupla é: {maior}")
