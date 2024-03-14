#import random
#number0 = random.randint(1, 10)
#print(number0)

from random import randint

def main():
    # Gera um número secreto entre 1 e 100
    numero_secreto = randint(1, 100)

    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100.")

    tentativas = 0
    while True:
        try:
            chute = int(input("Digite seu palpite: "))
            tentativas += 1

            if chute == numero_secreto:
                print(f"Parabéns! Você acertou em {tentativas} tentativas.")
                break
            elif chute < numero_secreto:
                print("Tente um número maior.")
            else:
                print("Tente um número menor.")
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()


