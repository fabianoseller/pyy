import random#Esta linha importa a biblioteca random, que fornece funções para gerar números aleatórios.

# Definindo o número secreto
numero_secreto = random.randint(1, 100)#Esta linha define a variável numero_secreto e gera um número aleatório entre 1 e 100 usando a função randint() da biblioteca random.

# Variável para armazenar o palpite do usuário
palpite = 0#Esta linha define a variável palpite e atribui o valor 0 a ela.
numeroTentativas = 0#Esta linha define a variável numeroTentativas e atribui o valor 0 a ela.

# Loop principal do jogo
print('********Você possui 3 tentativas para acertar o numero secreto!!!!!!!!!!!************')#Esta linha imprime uma mensagem no console informando o usuário que ele tem 3 tentativas para adivinhar o número secreto.
print(numero_secreto)
while numeroTentativas < 3 and palpite != numero_secreto: #Esta linha inicia um loop while que será executado enquanto numeroTentativas for menor ou igual a 3 e palpite for diferente de numero_secreto.
        # Solicitando o palpite do usuário
        palpite = int(input("Digite seu palpite: "))#Esta linha solicita ao usuário que digite seu palpite.A função input() captura a entrada do usuário como uma string.A função int() converte a string para um tipo de dado inteiro.O valor convertido é armazenado na variável palpite.
        
        numeroTentativas += 1#Esta linha incrementa o valor de numeroTentativas em 1.

        # Dando dicas ao usuário
        if palpite > numero_secreto:#Esta linha verifica se palpite é maior que numero_secreto.
            print("Seu palpite é maior que o número secreto.")#Se a condição for verdadeira, esta linha imprime uma mensagem no console informando que o palpite do usuário é maior que o número secreto.
        elif palpite < numero_secreto:#Esta linha verifica se palpite é menor que numero_secreto.
            print("Seu palpite é menor que o número secreto.")#Se a condição for verdadeira, esta linha imprime uma mensagem no console informando que o palpite do usuário é menor que o número secreto.


    # Mensagem de vitória
if palpite == numero_secreto or numeroTentativas < 3:#Esta linha verifica se palpite é igual a numero_secreto e numero de tentativas é menor que 3.
        print("Parabéns! Você adivinhou o número secreto!")#Se a condição  for verdadeira, esta linha imprime uma mensagem no console parabenizando o usuário por adivinhar o número secreto.
else:#Se a condição for falsa, este bloco de código é executado.
      print("Você não conseguiu adivinhar o número secreto. O número era", numero_secreto)#Esta linha imprime uma mensagem no console informando que o usuário não conseguiu adivinhar o número secreto e revela o número secreto.


