produtos = {}

# Adicionando produtos com input do usuário
while True:
    # Pede o nome do produto
    nome_produto = input("Digite o nome do produto: ")

    # Pede o preço do produto
    try:
        preco_produto = float(input("Digite o preço do produto: "))
    except ValueError:
        print("Preço inválido. Digite um número.")
        continue

    # Pede o estoque do produto
    try:
        estoque_produto = int(input("Digite o estoque do produto: "))
    except ValueError:
        print("Estoque inválido. Digite um número inteiro.")
        continue

    # Adiciona o produto ao dicionário
    produtos[nome_produto] = {"preço": preco_produto, "estoque": estoque_produto}

    # Pergunta se o usuário deseja continuar
    continuar = input("Deseja continuar adicionando produtos? (s/n) ")

    if not continuar.lower().startswith("s"):
        print(produtos)
        break
