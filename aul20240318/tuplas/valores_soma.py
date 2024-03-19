lista = [(3, 8, -1, 2), (2, -2, 4, 2), (7, 5, 3, -9)]
valores = []

# Calculando a soma dos valores não negativos em cada tupla e armazenando na lista 'valores'
sum_1 = sum(i for i in lista[0] if i >= 0) # Resulta: 13
sum_2 = sum(i for i in lista[1] if i >= 0) # Resulta: 8
sum_3 = sum(i for i in lista[2] if i >= 0) # Resulta: 15

valores.append(sum_1)
valores.append(sum_2)
valores.append(sum_3)

print("A sum_1: {}".format(sum_1))
print("A sum_2: {}".format(sum_2))
print("A sum_3: {}".format(sum_3))
