# Dicionário de frutas e preços
frutas_precos = {
    "banana": 2.50,
    "maçã": 1.75,
    "laranja": 2.00,
    "uva": 3.50,
    "morango": 4.00
}

# Imprimindo as chaves
print("Chaves:")
for chave in frutas_precos.keys():
    print(chave)

# Imprimindo os valores
print("\nValores:")
for valor in frutas_precos.values():
    print(valor)

# Imprimindo os pares chave-valor
print("\nPares chave-valor:")
for chave, valor in frutas_precos.items():
    print(f"{chave}: R${valor:.2f}")
