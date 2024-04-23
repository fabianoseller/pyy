tupla = (1, 2, 3, 4, 5)
elemento_remover = 3

tupla_nova = ()
for valor in tupla:
  if valor != elemento_remover:
    tupla_nova += (valor,)

print(f"Tupla original: {tupla}")
print(f"Elemento removido: {elemento_remover}")
print(f"Nova tupla: {tupla_nova}")
