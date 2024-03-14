# Importando a biblioteca random
import random

# Definindo o número secreto
numero_secreto = random.randint(1, 100)

# Variável para armazenar o palpite do usuário
palpite = 0

# Loop principal do jogo
while palpite != numero_secreto:
    # Solicitando o palpite do usuário
    palpite = int(input("Digite seu palpite: "))

    # Dando dicas ao usuário
    if palpite > numero_secreto:
        print("Seu palpite é maior que o número secreto.")
    elif palpite < numero_secreto:
        print("Seu palpite é menor que o número secreto.")

# Mensagem de vitória
print("Parabéns! Você adivinhou o número secreto!")
