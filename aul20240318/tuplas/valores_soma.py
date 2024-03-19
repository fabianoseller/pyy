lista = [(3, 8, -1, 2), (2, -2, 4, 2), (7, 5, 3, -9)]
valores = []
#Ou seja, criou-se uma tupla com os valores no índice 
#0 de cada lista, outra com os valores do índice
#1 e outra com os valores no índice 2. 
# Basta agora somarmos os valores quando os mesmos não 
# forem negativos, armazenando o resultado em variáveis, utilizando a função nativa sum.
sum_1 = sum(i for i in lista[0] if i >= 0) # Resulta: 13
sum_2 = sum(i for i in lista[1] if i >= 0) # Resulta: 8
sum_3 = sum(i for i in lista[2] if i >= 0) # Resulta: 15

#Ou seja, criou-se uma tupla com os valores no índice 0 de cada lista,
#outra com os valores do índice 1 e outra com os valores no índice 2. 
#Basta agora somarmos os valores quando os mesmos não forem negativos, 
#armazenando o resultado em variáveis, utilizando a função nativa sum.

print("A sum_1: {}".format(valores[sum_1]))
print("A sum_2: {}".format(valores[sum_2]))
print("A sum_3: {}".format(valores[sum_3]))