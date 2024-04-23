lista = [[3,2,7], [8,-2,5], [-1,4,3], [2,2,-9]]

valores = []

for coluna in range(len(lista[1])):
    soma = 0

    for linha in range(len(lista)):
        if(lista[linha][coluna] >= 0):
            soma += lista[linha][coluna]

    valores.append(soma)

print(valores)