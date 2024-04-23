# lista = [(3, 8, -1, 2), (2, -2, 4, 2), (7, 5, 3, -9)]
# indices_menores_valores = []

# # Encontrando a posição do menor valor em cada tupla
# for tupla in lista:
#     indice_menor_valor = tupla.index(min(tupla))
#     indices_menores_valores.append(indice_menor_valor)

# print("As posições dos menores valores em cada tupla são:")
# for i, indice in enumerate(indices_menores_valores, 1):
#     print(f"Tupla {i}: Índice {indice}")

lista = [(3, 8, -1, 2), (2, -2, 4, 2), (7, 5, 3, -9)]

# Encontrando o menor valor e sua posição em cada tupla
for i, tupla in enumerate(lista, 1):
    menor_valor = min(tupla)
    indice_menor_valor = tupla.index(menor_valor)
    print(f"Na Tupla {i}: O menor valor é {menor_valor} e está na posição {indice_menor_valor}")
