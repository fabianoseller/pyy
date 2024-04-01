conjunto = {1, 2, 3, 4, 5}
tentativas = 0
while True:
    tentativa = int(input("Tente adivinhar um número do conjunto: "))
    tentativas += 1
    if tentativa in conjunto:
        print("Parabéns! Você acertou o número.")
        break
    else:
        print("Tente novamente.")