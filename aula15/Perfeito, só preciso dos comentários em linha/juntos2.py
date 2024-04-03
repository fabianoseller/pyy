# Ordenação decrescente
numeros = {5, 9, 2, 7, 1, 8, 3, 10, 6, 4}

# Ordenação crescente
ordenado_crescente = []
for i in range(1, max(numeros)+1):
    if i in numeros:
        ordenado_crescente.append(i)

# Ordenação decrescente
ordenado_decrescente = []
for i in range(max(numeros), 0, -1):
    if i in numeros:
        ordenado_decrescente.append(i)

print("Ordenado em ordem crescente:", ordenado_crescente)
print("Ordenado em ordem decrescente:", ordenado_decrescente)
