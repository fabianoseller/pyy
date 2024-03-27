# 1. Encontrar o Maior Valor em uma Lista:
lista = [5, 3, 8, 1, 10]
maior_valor = max(lista)
print("O maior valor na lista é:", maior_valor)
print("********")

# 2. Encontrar a Soma dos Valores em uma Lista:
lista = [5, 3, 8, 1, 10]
soma = sum(lista)
print("A soma dos valores na lista é:", soma)
print("********")

# 3. Encontrar a Média dos Valores em uma Lista:
lista = [5, 3, 8, 1, 10]
media = sum(lista) / len(lista)
print("A média dos valores na lista é:", media)
print("********")

# 4. Encontrar a Posição do Menor Valor em uma Lista:
lista = [5, 3, 8, 1, 10]
posicao_menor = lista.index(min(lista))
print("A posição do menor valor na lista é:", posicao_menor)
print("********")

# 5. Encontrar a Posição do Maior Valor em uma Lista:
lista = [5, 3, 8, 1, 10]
posicao_maior = lista.index(max(lista))
print("A posição do maior valor na lista é:", posicao_maior)
print("********")

# 6. Encontrar o Número de Vezes que um Valor Aparece em uma Lista:
lista = [1, 2, 3, 2, 1, 2, 4, 5, 2]
valor = 2
ocorrencias = lista.count(valor)
print("O valor", valor, "aparece", ocorrencias, "vezes na lista.")
print("********")

# 7. Verificar se um Valor Está Presente em uma Lista:
lista = [1, 2, 3, 4, 5]
valor = 3
if valor in lista:
    print("O valor", valor, "está presente na lista.")
else:
    print("O valor", valor, "não está presente na lista.")
print("********")

# 8. Gerar uma Lista com Valores Pares de 1 a 10:
lista_pares = [i for i in range(1, 11) if i % 2 == 0]
print("Lista de valores pares de 1 a 10:", lista_pares)
print("********")

# 9. Gerar uma Lista com Valores Ímpares de 1 a 10:
lista_impares = [i for i in range(1, 11) if i % 2 != 0]
print("Lista de valores ímpares de 1 a 10:", lista_impares)
print("********")

# 10. Inverter a Ordem dos Elementos de uma Lista:
lista = [1, 2, 3, 4, 5]
lista_invertida = lista[::-1]
print("Lista invertida:", lista_invertida)
print("********")

# 11. Concatenar Duas Listas:
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_concatenada = lista1 + lista2
print("Lista concatenada:", lista_concatenada)
print("********")

# 12. Dividir uma Lista em Duas:
lista = [1, 2, 3, 4, 5, 6]
metade = len(lista) // 2
lista1 = lista[:metade]
lista2 = lista[metade:]
print("Primeira metade da lista:", lista1)
print("Segunda metade da lista:", lista2)
print("********")

# 13. Ordenar os Elementos de uma Lista:
lista = [5, 2, 8, 1, 3]
lista_ordenada = sorted(lista)
print("Lista ordenada:", lista_ordenada)
print("********")

# 14. Remover um Elemento de uma Lista:
lista = [1, 2, 3, 4, 5]
valor = 3
lista.remove(valor)
print("Lista após remover o valor", valor, ":", lista)
print("********")

# 15. Adicionar um Elemento a uma Lista:
lista = [1, 2, 3, 4]
valor = 89
lista.append(valor)
print("Lista após adicionar o valor", valor, ":", lista)
