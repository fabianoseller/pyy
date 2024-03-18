import os

# Função para exibir o menu e obter a escolha do usuário
def exibir_menu():
    print("\n=== Simulador de Caixa Eletrônico ===")
    print("1. Ver Saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Sair")

    escolha = input("Escolha uma opção: ")
    return escolha

# Função para carregar o saldo do arquivo
def carregar_saldo():
    try:
        # Obter o diretório do arquivo Python em execução
        diretorio_atual = os.path.dirname(__file__)
        arquivo_saldo = os.path.join(diretorio_atual, "saldo.txt")
        with open(arquivo_saldo, "r") as file:
            return float(file.read())
    except FileNotFoundError:
        # Se o arquivo não existir, cria ele com saldo inicial zero
        with open(arquivo_saldo, "w") as file:
            file.write("0")
        return 0

# Função para salvar o saldo no arquivo
def salvar_saldo(saldo):
    # Obter o diretório do arquivo Python em execução
    diretorio_atual = os.path.dirname(__file__)
    arquivo_saldo = os.path.join(diretorio_atual, "saldo.txt")
    with open(arquivo_saldo, "w") as file:
        file.write(str(saldo))

# Inicializando o saldo
saldo = carregar_saldo()

# Loop principal do programa
while True:
    opcao = exibir_menu()

    if opcao == "1":
        print(f"Seu saldo atual é: R${saldo}")
    elif opcao == "2":
        valor_deposito = float(input("Digite o valor que deseja depositar: R$"))
        saldo += valor_deposito
        salvar_saldo(saldo)
        print(f"R${valor_deposito} depositado com sucesso. Seu saldo atual é: R${saldo}")
    elif opcao == "3":
        valor_saque = float(input("Digite o valor que deseja sacar: R$"))
        if valor_saque > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= valor_saque
            salvar_saldo(saldo)
            print(f"Saque de R${valor_saque} realizado com sucesso. Seu saldo atual é: R${saldo}")
    elif opcao == "4":
        print("Obrigado por usar o Simulador de Caixa Eletrônico. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
