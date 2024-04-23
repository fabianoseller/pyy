#Variáveis
nome = "Seu nome"
idade = 20

print(nome, idade)
########################################################################################################
#Tipos de dados
numero_inteiro = 10
numero_real = 3.14
texto = "Olá, mundo!"
complex = 1 + 2j
print(type(numero_inteiro))
print(type(numero_real))
print(type(texto))
print(type(complex))
########################################################################################################
#Outros tipos de dados:
# Lista de nomes
nomes = ["Ana", "João", "Maria"]

# Tupla de coordenadas
coordenadas = (10, 20, 30)

# Dicionário de telefones
telefones = {"Ana": "1234-5678", "João": "9876-5432"}

# Set de cores
cores = {"azul", "verde", "vermelho"}

# Imprimindo os valores
print(nomes)
print(coordenadas)
print(telefones)
print(cores)

########################################################################################################
#Condicionais
numero = 10

if numero > 5:
  print("O número é maior que 5")
else:
  print("O número é menor ou igual a 5")
########################################################################################################
#laços
  for i in range(5):
    print(i)

numero = 1
while numero <= 5:
  print(numero)
  numero += 1
########################################################################################################
#Operadores Aritméticos
# + adição
# - subtração
# * multiplicação
# / divisão
# % resto da divisão 
# ** exponenciação
#// divisão inteira
 
soma = 1 + 2
diferenca = 5 - 3
multiplicacao = 4 * 2
divisao = 10 / 2
resto_da_divisão = 10 % 2
exponenciação=10**2
divisão_inteira=10//2

print(soma, diferenca, multiplicacao, divisao,resto_da_divisão,exponenciação,divisão_inteira)
########################################################################################################
#Operadores Lógicos
# and
# or
# not
x = 10
y = 5

resultado = x > 0 and y < 10

print(f"Resultado: {resultado}")



x = 0
y = 10

resultado = x > 0 or y < 10

print(f"Resultado: {resultado}")


x = True

resultado = not x

print(f"Resultado: {resultado}")
########################################################################################################
#Operadores comparativos
# < menor
# <= menor ou igual
# > maior
# >= maior ou igual
# == igual 
# != ou <> diferente
x = 10
y = 10
igualdade = x == y
print(igualdade)  



desigualdade = x != 5
print(desigualdade)



menor_que = 3 < 5
print(menor_que)

menor_igual = 4 <= 4
print(menor_igual)


maior_que = 7 > 2
print(maior_que)


maior_igual = 8 >= 8
print(maior_igual) 
########################################################################################################
#Formatação de Strings
#str %s
nome = "Alice"
idade = 30

saudação = "Olá, %s! Você tem %d anos de idade." % (nome, idade)
print(saudação)  # Saída: Olá, Alice! Você tem 30 anos de idade.
#int %d
numero = 123

numero_formatado = "O número é %d." % numero
print(numero_formatado)  # Saída: O número é 123.
#float %f
pi = 3.1415926535

pi_formatado = "O valor de pi é aproximadamente %.2f." % pi
print(pi_formatado)  # Saída: O valor de pi é aproximadamente 3.14.

# Especificando Casas Decimais para `%f`:

pi_formatado_3_casas = "O valor de pi é aproximadamente %.3f." % pi
print(pi_formatado_3_casas)  # Saída: O valor de pi é aproximadamente 3.142.
########################################################################################################
idade = int(input("Digite uma idade: "))
nome = input("Nome da primeira pessoa: ")
salario = float(input("Salario da primeira pessoa: "))
########################################################################################################
#Conversão de tipos básicos:
#Inteiro para string
numero = 123
texto = str(numero)

print(f"Número: {numero}, Tipo: {type(numero)}")
print(f"Texto: {texto}, Tipo: {type(texto)}")
########################################################################################################
#String para float
valor_texto = "3.1415"
valor_numerico = float(valor_texto)

print(f"Texto: {valor_texto}, Tipo: {type(valor_texto)}")
print(f"Número: {valor_numerico}, Tipo: {type(valor_numerico)}")
########################################################################################################
#Booleano para string:
verdadeiro = True
texto_booleano = str(verdadeiro)

print(f"Valor booleano: {verdadeiro}, Tipo: {type(verdadeiro)}")
print(f"Texto: {texto_booleano}, Tipo: {type(texto_booleano)}")
########################################################################################################
#Concatenação
idade=31
nome="Lucas" 
altura=1.80
professor=True

print('minha idade é:', idade)
print(f'minha idade é: {idade}')
print('minha idade é:', str(idade))
print('minha idade é: {}'.format(idade))
primeira_string = "Olá"
segunda_string = "mundo!"

mensagem_completa = primeira_string + " " + segunda_string

print(mensagem_completa)
nome1 = "João"
idade1 = 20

mensagem_com_f_string = f"Olá, {nome1}. Você tem {idade1} anos."

print(mensagem_com_f_string)
idade2 = 20

mensagem_com_str = "Olá, você tem " + str(idade2) + " anos."

print(mensagem_com_str)
idade3 = 20

mensagem_com_format = "Olá, você tem {} anos.".format(idade3)

print(mensagem_com_format)
idade = 25
nome = "Ana"

# Formatação básica
print(f"Olá, {nome}, sua idade é {idade}.")

# Formatação avançada
print(f"Olá, {nome}, você tem {idade:02d} anos.")