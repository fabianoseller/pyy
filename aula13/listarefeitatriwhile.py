# 01 Encontrar o Maior Valor em uma Lista
lista = []
while True:
    tecla_parada = input("Pressione uma tecla para parar de agregar números à lista: ")
    if not tecla_parada.isdigit():
        break
    else:
        print("Digite uma tecla, não um número.")

print("Sua tecla para parar é:", tecla_parada)
while True:
    valor = input("Digite um número inteiro e pressione enter para agregar o valor à lista (ou pressione {} para parar): ".format(tecla_parada))
    if valor == tecla_parada:
        break
    try:
        numero = int(valor)
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")
    else:
        lista.append(numero)

if lista != []:
    print("Lista de números inteiros:", lista)
else:
    print("Sua lista está vazia")

try:
    maior_valor = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > maior_valor:
            maior_valor = lista[i]
    print(f"O maior valor é: {maior_valor}")
    # simplificação
    print(f"O maior valor é: {max(lista)}")
except ValueError:
    print("Para saber o maior valor, a lista deve ter pelo menos um elemento")

# 02 Encontrar a Soma dos Valores em uma Lista
try:
    soma = sum(lista)
    print(f"A soma dos valores na lista é: {soma}")
except ValueError:
    print("Não é possível calcular a soma. A lista está vazia.")

# 03 Encontrar a Média dos Valores em uma Lista
try:
    media = sum(lista) / len(lista)
    print(f"A média dos valores na lista é: {media}")
except ValueError:
    print("Não é possível calcular a média. A lista está vazia.")
except ZeroDivisionError:
    print("Não é possível calcular a média. A lista está vazia.")

# 04 Encontrar a Posição do Menor Valor em uma Lista
lista = []
while True:
    tecla_parada = input("Pressione uma tecla para parar de adicionar números à lista: ")
    if not tecla_parada.isdigit():
        break
    else:
        print("Digite uma tecla, não um número.")

print("Sua tecla para parar é:", tecla_parada)
while True:
    valor = input("Digite um número inteiro e pressione enter para adicionar o valor à lista (ou pressione {} para parar): ".format(tecla_parada))
    if valor == tecla_parada:
        break
    try:
        numero = int(valor)
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")
    else:
        lista.append(numero)

if lista:
    print("Lista de números inteiros:", lista)
    try:
        menor_valor = lista[0]
        posicao_menor = 0
        for i in range(1, len(lista)):
            if lista[i] < menor_valor:
                menor_valor = lista[i]
                posicao_menor = i
        print(f"A posição do menor valor na lista é: {posicao_menor}")
    except ValueError:
        print("Para encontrar a posição do menor valor, a lista deve ter pelo menos um elemento")
else:
    print("Sua lista está vazia")

# 05 Encontrar a Posição do Maior Valor em uma Lista
if lista:
    try:
        maior_valor = lista[0]
        posicao_maior = 0
        for i in range(1, len(lista)):
            if lista[i] > maior_valor:
                maior_valor = lista[i]
                posicao_maior = i
        print(f"A posição do maior valor na lista é: {posicao_maior}")
    except ValueError:
        print("Para encontrar a posição do maior valor, a lista deve ter pelo menos um elemento")
else:
    print("Sua lista está vazia")

# 06 Encontrar o Número de Vezes que um Valor Aparece em uma Lista
if lista:
    try:
        valor = int(input("Digite um valor para encontrar o número de vezes que aparece na lista: "))
        vezes = lista.count(valor)
        print(f"O valor {valor} aparece {vezes} vezes na lista.")
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")
else:
    print("Sua lista está vazia")

# 07 Verificar se um Valor Está Presente em uma Lista
if lista:
    try:
        valor = int(input("Digite um valor para verificar se está presente na lista: "))
        if valor in lista:
            print(f"O valor {valor} está presente na lista.")
        else:
            print(f"O valor {valor} não está presente na lista.")
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")
else:
    print("Sua lista está vazia")

# 08 Gerar uma Lista com Valores Pares de 1 a 10
lista_pares = []
for i in range(2, 11, 2):
    lista_pares.append(i)
print("Lista de valores pares de 1 a 10:", lista_pares)

# 09 Gerar uma Lista com Valores Ímpares de 1 a 10
lista_impares = []
for i in range(1, 11, 2):
    lista_impares.append(i)
print("Lista de valores ímpares de 1 a 10:", lista_impares)

# 10. Inverter a Ordem dos Elementos de uma Lista
if lista:
    lista_invertida = lista[::-1]
    print("Lista invertida:", lista_invertida)
else:
    print("Sua lista está vazia")

# 11. Concatenar Duas Listas
outra_lista = [11, 22, 33]
lista_concatenada = lista + outra_lista
print("Lista concatenada:", lista_concatenada)

# 12. Dividir uma Lista em Duas
if lista:
    tamanho = len(lista)
    metade = tamanho // 2
    primeira_metade = lista[:metade]
    segunda_metade = lista[metade:]
    print("Primeira metade da lista:", primeira_metade)
    print("Segunda metade da lista:", segunda_metade)
else:
    print("Sua lista está vazia")

# 13. Ordenar os Elementos de uma Lista
if lista:
    lista_ordenada = sorted(lista)
    print("Lista ordenada:", lista_ordenada)
else:
    print("Sua lista está vazia")

# 14. Remover um Elemento de uma Lista
if lista:
    try:
        valor_remover = int(input("Digite o valor a ser removido da lista: "))
        if valor_remover in lista:
            lista.remove(valor_remover)
            print(f"Valor {valor_remover} removido da lista.")
            print("Lista atualizada:", lista)
        else:
            print(f"O valor {valor_remover} não está presente na lista.")
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")
else:
    print("Sua lista está vazia")

# 15. Adicionar um Elemento a uma Lista
novo_elemento = input("Digite um novo elemento para adicionar à lista: ")
lista.append(novo_elemento)
print("Lista atualizada:", lista)
