#Verificando chaves e valores:


# se entnedi: Verifica se uma palavra existe como chave em um dicionário de sinônimos.
# Conta o número de ocorrências de cada letra em uma string usando um dicionário.
# Remove do dicionário todas as chaves que possuem valores vazios.

# Verificando se uma palavra existe como chave em um dicionário de sinônimos

# Verificando se uma palavra existe como chave em um dicionário de sinônimos



# Verificando se uma palavra existe como chave em um dicionário de sinônimos relacionados ao mar
print("Verificar se uma palavra existe como chave em um dicionário de sinônimos relacionados ao mar:")
dicionario_sinonimos = {
    "ondulado": ["agitação", "movimento"],
    "sereno": ["calmo", "tranquilo"],
    "barco": ["embarcação", "navio"]
}

palavra = input("Digite uma palavra para verificar se existe como chave no dicionário de sinônimos: ")
if palavra in dicionario_sinonimos:
    print(f"A palavra '{palavra}' existe como chave no dicionário de sinônimos.")
else:
    print(f"A palavra '{palavra}' não existe como chave no dicionário de sinônimos.")

# Contando o número de ocorrências de cada letra em uma string usando um dicionário
print("\nContar o número de ocorrências de cada letra em uma string:")
string = input("Digite uma string para contar o número de ocorrências de cada letra: ")
contagem_letras = {}
for letra in string:
    if letra.isalpha():  # Verifica se o caractere é uma letra
        contagem_letras[letra] = contagem_letras.get(letra, 0) + 1

print("Contagem de ocorrências de cada letra:")
for letra, contagem in contagem_letras.items():
    print(f"{letra}: {contagem}")

# Removendo do dicionário todas as chaves que possuem valores vazios
print("\nRemover do dicionário todas as chaves que possuem valores vazios:")
dicionario_pecas_barco = {
    "motor": "Yamaha",
    "hélice": "",
    "leme": "Volvo",
    "vela": "",
    "âncora": "Lewmar",
    "bússola": "",
    "proa": "Acme",
    "popa": "XYZ",
    "leme": "Volvo",
    "catraca": "Johnson",
    "ponte": "Sunseeker",
    "viga": "Mitsubishi",
    "porão": "Marine",
    "cabine": "Sealine",
    "costado": "Princess",
    "guincho": "Goiot",
    "convés": "Bavaria",
    "escotilha": "Beneteau",
    "bujão": "Regal"
}

print("Dicionário de peças de barco antes da remoção de chaves com valores vazios:")
print(dicionario_pecas_barco)

dicionario_pecas_barco = {chave: valor for chave, valor in dicionario_pecas_barco.items() if valor != ""}

print("\nDicionário de peças de barco após a remoção de chaves com valores vazios:")
print(dicionario_pecas_barco)

