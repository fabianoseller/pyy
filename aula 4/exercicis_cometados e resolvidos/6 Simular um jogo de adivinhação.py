#Simular um jogo de adivinhação:
# Operador de comparação de igualdade (==)

numero_secreto = 7#Esta linha define o número secreto como 7.

numero_digitado = int(input("Digite um número: "))#Esta linha solicita ao usuário que digite um número e armazena o valor digitado na variável "numero_digitado". A função int() converte o valor digitado para um número inteiro.

if numero_digitado == numero_secreto:#Esta linha verifica se o número digitado pelo usuário é igual ao número secreto. Se forem iguais, o bloco de código dentro do if será executado.
  print("Você adivinhou o número secreto!")#Se o número digitado for igual ao número secreto, esta linha imprime uma mensagem informando o usuário que ele adivinhou o número.
else:#Se o número digitado não for igual ao número secreto, o bloco de código dentro do else será executado.
  print("Você errou o número secreto. Tente novamente!")#Se o número digitado não for igual ao número secreto, esta linha imprime uma mensagem informando o usuário que ele errou o número e que deve tentar novamente.