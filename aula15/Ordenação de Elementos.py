
#Crie um conjunto com números de 1 a 10.
#Ordene os elementos do conjunto em ordem crescente e decrescente e imprima as listas ordenadas.


# Ordenação de Elementos
numeros = {9, 3, 1, 6, 8, 2, 7, 5, 4, 10}
numeros_crescente = sorted(numeros)
numeros_decrescente = sorted(numeros, reverse=True)
print("Ordem crescente:", numeros_crescente)
print("Ordem decrescente:", numeros_decrescente)
