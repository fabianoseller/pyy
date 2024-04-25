#seguida, utilize os métodos keys(), values() e items() para imprimir as chaves, valores e pares chave-valor do dicionário, respectivamente.
frutas = {
    "banana": 2.50,
    "maçã": 3.00,
    "laranja": 1.50,
    "uva": 4.00,
    "mamão": 5.00,
}

# Imprimindo as chaves do dicionário
print("**Chaves:**")
for chave in frutas.keys():
    print(chave)

# Imprimindo os valores do dicionário
print("\n**Valores:**")
for valor in frutas.values():
    print(valor)

# Imprimindo os pares chave-valor do dicionário
print("\n**Pares Chave-Valor:**")
for chave, valor in frutas.items():
    print(f"Chave: {chave}, Valor: {valor}")