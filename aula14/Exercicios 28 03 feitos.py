# 1. Verificação de elemento em conjunto
conjunto = {1, 2, 3, 4, 5}
elemento = int(input("Digite um número para verificar se está presente no conjunto: "))
if elemento in conjunto:
    print(f"O elemento {elemento} está presente no conjunto.")
else:
    print(f"O elemento {elemento} não está presente no conjunto.")

# 2. Interseção de conjuntos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
intersecao = set()
for elemento in conjunto1:
    if elemento in conjunto2:
        intersecao.add(elemento)
print("A interseção dos conjuntos é:", intersecao)

# 3. Diferença de conjuntos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
diferenca = set()
for elemento in conjunto1:
    if elemento not in conjunto2:
        diferenca.add(elemento)
print("A diferença entre os conjuntos é:", diferenca)

# 4. União de conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
uniao = conjunto1.copy()
for elemento in conjunto2:
    uniao.add(elemento)
print("A união dos conjuntos é:", uniao)

# 5. Subconjuntos
conjunto1 = {1, 2}
conjunto2 = {1, 2, 3, 4, 5}
subconjunto = True
for elemento in conjunto1:
    if elemento not in conjunto2:
        subconjunto = False
        break
if subconjunto:
    print("O conjunto 1 é subconjunto do conjunto 2.")
else:
    print("O conjunto 1 não é subconjunto do conjunto 2.")

# 6. Ordenação de elementos em um conjunto
conjunto = {3, 1, 4, 2, 5}
ordenado = sorted(conjunto)
print("Conjunto ordenado em ordem crescente:", ordenado)
ordenado_inverso = sorted(conjunto, reverse=True)
print("Conjunto ordenado em ordem decrescente:", ordenado_inverso)

# 7. Remoção de elementos duplicados
conjunto = {1, 2, 2, 3, 3, 4, 5}
sem_duplicados = set()
for elemento in conjunto:
    if elemento not in sem_duplicados:
        sem_duplicados.add(elemento)
print("Conjunto sem elementos duplicados:", sem_duplicados)

# 8. Jogo de adivinhação com conjunto
conjunto = {1, 2, 3, 4, 5}
tentativas = 0
while True:
    tentativa = int(input("Tente adivinhar um número do conjunto: "))
    tentativas += 1
    if tentativa in conjunto:
        print("Parabéns! Você acertou o número.")
        break
    else:
        print("Tente novamente.")

# 9. Cálculo de média, mediana e moda de um conjunto
conjunto = {1, 2, 2, 3, 3, 3, 4, 4, 5, 5}
numeros_ordenados = sorted(conjunto)
tamanho = len(numeros_ordenados)
media = sum(numeros_ordenados) / tamanho
mediana = numeros_ordenados[tamanho // 2] if tamanho % 2 != 0 else (numeros_ordenados[tamanho // 2 - 1] + numeros_ordenados[tamanho // 2]) / 2
frequencia = {numero: numeros_ordenados.count(numero) for numero in conjunto}
moda = max(frequencia, key=frequencia.get)
print("Média:", media)
print("Mediana:", mediana)
print("Moda:", moda)
