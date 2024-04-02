
#Crie um conjunto com números de 1 a 10.
#Ordene os elementos do conjunto em ordem crescente e decrescente e imprima as listas ordenadas.

numeros = {4, 2, 7, 1, 9, 5, 3, 10, 8, 6}

# Ordenação crescente
numeros_crescente = sorted(numeros)
print("Ordem crescente:", numeros_crescente)

# Ordenação decrescente
numeros_decrescente = sorted(numeros, reverse=True)
print("Ordem decrescente:", numeros_decrescente)
