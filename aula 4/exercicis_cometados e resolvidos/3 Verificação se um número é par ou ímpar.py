 #Verificação se um número é par ou ímpar:
  # Operador de módulo (%)

numero = int(input("Digite um número: "))#Esta linha solicita ao usuário que digite um número e armazena o valor digitado na variável numero.A função int() converte o valor digitado para um número inteiro.

if numero % 2 == 0:#Esta linha verifica se o resto da divisão do número por 2 é igual a 0. Se o resto for igual a 0, o número é par e o bloco de código dentro do if será executado.
  print("O número é par.")#Se o número for par, esta linha imprime uma mensagem informando o usuário.
else:#Se o resto da divisão do número por 2 não for igual a 0, o bloco de código dentro do else será executado.
  print("O número é ímpar.")#Se o número for ímpar, esta linha imprime uma mensagem informando o usuário.