lista = [(3, 8, -1, 2), (2, -2, 4, 2), (7, 5, 3, -9)]

# Lista para armazenar os elementos em ordem crescente
ordem_crescente = []

# Lista para armazenar os elementos em ordem decrescente
ordem_decrescente = []

# Iterando sobre cada tupla na lista
for tupla in lista:
    #  ordem crescente e adicionando à lista correspondente
    ordem_crescente.append(tuple(sorted(tupla)))

    # elementos em ordem decrescente e adicionando à lista correspondente
    ordem_decrescente.append(tuple(sorted(tupla, reverse=True)))

# Exibindo os resultados
print("Lista Original posicionados:\n\n", lista, "\n")

print("Lista em ordem crescente:", ordem_crescente)
print("Lista em ordem decrescente:", ordem_decrescente)
