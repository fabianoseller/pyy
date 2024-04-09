# Criar um dicionário vazio

#update foi adicionado para incluir os animais iniciais 
# no dicionário animais_sons antes de entrar no loop do
# menu. Isso garante que todos os animais estejam presentes no dicionário desde o início.

# Criar um dicionário vazio
animais_sons = {}

def visualizar_dicionario(dicionario):
    """Função para visualizar o dicionário atualizado."""
    print("\nDicionário de animais e sons:")
    if dicionario:
        for animal, som in dicionario.items():
            print(f"{animal}: {som}")
    else:
        print("O dicionário está vazio.")

def adicionar_animal():
    """Função para adicionar um novo animal e seu som."""
    while True:
        animal = input("Digite o nome do animal: ")
        if animal in animais_sons:
            print("Esse animal já foi digitado. Por favor, escolha outro animal.")
            continue
        som = input("Digite o som do animal: ")

        # Verificar se o som já está presente no dicionário
        if som not in animais_sons.values():
            animais_sons[animal] = som
            print("Par chave-valor adicionado com sucesso!")
        else:
            print("Esse som já foi atribuído a outro animal. Por favor, escolha outro som.")

        continuar = input("Deseja adicionar outro par chave-valor? (S/N): ").upper()
        if continuar != "S":
            break

def menu():
    """Função para exibir o menu principal."""
    print("\nMENU:")
    print("1. Visualizar dicionário de animais e sons")
    print("2. Adicionar novo animal e som")
    print("3. Sair do programa")

# Adicionar pares chave-valor para 13 animais
animais_iniciais = {
    "Cachorro": "Au",
    "Gato": "Miau",
    "Vaca": "Muu",
    "Pato": "Quack",
    "Galinha": "Cocoricó",
    "Leão": "Rugido",
    "Elefante": "Barulho de tromba",
    "Cavalo": "Relincho",
    "Macaco": "Grito",
    "Girafa": "Rugido suave",
    "Tigre": "Rugido forte",
    "Urso": "Rugido bruto",
    "Coelho": "Ronco suave"
}
animais_sons.update(animais_iniciais)  # Adicionando os animais iniciais ao dicionário

# Menu principal
while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        visualizar_dicionario(animais_sons)cd py
    elif opcao == "2":
        adicionar_animal()
    elif opcao == "3":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
