tupla = (5, 2, 4, 1, 3)

# Ordenar em ordem crescente
tupla_ordenada = tuple(sorted(tupla))

# Ordenar em ordem decrescente
tupla_ordenada_decrescente = tuple(sorted(tupla, reverse=True))

print(f"Tupla original: {tupla}")
print(f"Tupla ordenada (crescente): {tupla_ordenada}")
print(f"Tupla ordenada (decrescente): {tupla_ordenada_decrescente}")
