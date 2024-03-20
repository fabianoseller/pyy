tupla = ("a", "b", "c", "a", "b", "a")
valor_procurado = "a"
contagem = 0
for elemento in tupla:
  if elemento == valor_procurado:
    contagem += 1

print(f"O valor '{valor_procurado}' aparece {contagem} vezes na tupla")
