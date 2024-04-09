#. Iterando sobre dicionários


# Dicionário com informações de contato
informacoes_contato = {
    "João": {"telefone": "123456789", "email": "joao@example.com"},
    "Maria": {"telefone": "987654321", "email": "maria@example.com"},
    "Pedro": {"telefone": "999999999", "email": "pedro@example.com"}
}

# Percorrendo o dicionário de informações de contato e imprimindo cada item
print("Informações de contato:")
for nome, info in informacoes_contato.items():
    print(f"Nome: {nome}")
    print(f"Telefone: {info['telefone']}")
    print(f"Email: {info['email']}")
    print()

# Dicionário com preços das peças de carro
precos_pecas = {
    "pneu": 250.0,
    "farol": 120.0,
    "bateria": 300.0,
    "freio": 150.0
}

# Calculando a soma dos preços das peças de carro
soma_precos_pecas = sum(precos_pecas.values())
print("Soma dos preços das peças de carro:", soma_precos_pecas)

# Dicionário original
dicionario_original = {"parafuso": 1, "porca": 2, "arruela": 3, "buchas": 4, "molas": 5}

# Valor para comparar
valor_limite = 2

# Criando um novo dicionário com chaves maiores que o valor limite
novo_dicionario = {chave: valor for chave, valor in dicionario_original.items() if valor > valor_limite}

print("\nNovo dicionário com chaves maiores que", valor_limite, ":")
print(novo_dicionario)