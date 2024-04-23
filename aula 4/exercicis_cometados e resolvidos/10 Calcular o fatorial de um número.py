#Calcular o fatorial de um número:
# Operador de multiplicação (*)

numero = int(input("Digite um número: "))#Esta linha solicita ao usuário que digite um número e armazena o valor digitado na variável "numero". A função int() converte o valor digitado para um número inteiro.

fatorial = 1#Esta linha define a variável "fatorial" e a inicializa com o valor 1. O fatorial de 0 é 1, por isso é importante inicializar a variável com este valor.

for i in range(1, numero + 1):#Esta linha inicia um loop for que irá iterar de 1 até o valor armazenado na variável "numero". A variável "i" é utilizada para controlar a iteração do loop.
  fatorial *= i#Dentro do loop for, esta linha multiplica o valor atual da variável "fatorial" pelo valor da variável "i".

print(f"O fatorial de {numero} é: {fatorial}")#Esta linha imprime o resultado do fatorial do número digitado pelo usuário. A função f-string é utilizada para formatar a string de saída.
