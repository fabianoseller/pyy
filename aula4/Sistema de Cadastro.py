#Referencias:

##Ainda em desenvolvimento
#Controle de estoque:
#Crie um sistema de controle de estoque com as operações de entrada, saída e 
#consulta de produtos usando while
#https://pt.stackoverflow.com/questions/555689/sistema-de-cadastro-e-login-python

# https://sentry.io/answers/raise-an-exception-in-python/

# Inicializando o dicionário para armazenar os produtos e suas quantidades
import json
import os.path

# Função para verificar se o arquivo "estoque.json" existe e criar se não existir
def criar_arquivo_estoque():
    if not os.path.isfile("estoque.json"):
        with open("estoque.json", "w") as file:
            json.dump({}, file)

# Inicializando o dicionário para armazenar os produtos e suas quantidades
estoque = {}

# Função para carregar os dados do estoque de um arquivo JSON
def carregar_estoque():
    with open("estoque.json", "r") as file:
        return json.load(file)

# Função para salvar os dados do estoque em um arquivo JSON
def salvar_estoque():
    with open("estoque.json", "w") as file:
        json.dump(estoque, file)

# Função para adicionar produtos ao estoque
def entrada_produto():
    produto = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    if produto in estoque:
        estoque[produto] += quantidade
    else:
        estoque[produto] = quantidade
    print(f"{quantidade} unidades de {produto} adicionadas ao estoque.")
    salvar_estoque()

# Função para remover produtos do estoque
def saida_produto():
    produto = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto a ser retirada: "))
    if produto in estoque and estoque[produto] >= quantidade:
        estoque[produto] -= quantidade
        print(f"{quantidade} unidades de {produto} retiradas do estoque.")
        salvar_estoque()
    else:
        print("Produto não encontrado ou quantidade insuficiente em estoque.")

# Função para consultar a quantidade de um produto no estoque
def consulta_produto():
    produto = input("Digite o nome do produto: ")
    if produto in estoque:
        print(f"A quantidade de {produto} em estoque é: {estoque[produto]}")
    else:
        print("Produto não encontrado.")

# Verificar e criar o arquivo "estoque.json" se ele não existir
criar_arquivo_estoque()

# Carregar os dados do estoque do arquivo JSON ao iniciar o programa
estoque = carregar_estoque()

# Loop principal do programa
while True:
    print("\n=== Sistema de Controle de Estoque ===")
    print("1. Entrada de Produto")
    print("2. Saída de Produto")
    print("3. Consulta de Produto")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        entrada_produto()
    elif opcao == "2":
        saida_produto()
    elif opcao == "3":
        consulta_produto()
    elif opcao == "4":
        print("Saindo do sistema de controle de estoque...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
