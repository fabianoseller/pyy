print("A aranha pequenininha\nsubiu a tromba d'água.")
print()
print("abaixo veio a chuva\ne lavou a aranha.")

print("A aranha pequenininha\nsubiu a tromba d'água.")
print()
print("abaixo veio a chuva\ne lavou a aranha.")


print("A aranha pequenininha" , "subiu" , "a tromba d'água.")

print("Meu nome é", "Python.")
print("Monty Python.")

print("Meu nome é", "Python.", end=" ")
print("Monty Python.")

print("Meu nome é ", end="")
print("Monty Python.")


print("Meu nome é ", end="")
print("Monty Python.")

print("Meu", "nome", "é", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")


#Programação***Essenciais***em...Python

print("Programação","Essenciais","em", sep="***", end="...")
print("Python")

print(" *")
print(" * *")
print(" * *")
print(" * *")
print("*** ***")
print(" * *")

print(" * *")
print(" *****")

print("Meu\nnome\né\nBond.", end=" ")
print("James Bond.")

#print(sep="&", "peixe", "salgadinhos")
#Lembre-se: Os argumentos de palavras-chave devem ser passados após quaisquer argumentos posicionais obrigatórios.

print('Greg\'s book.')
print("'Greg's book.'")
print('"Greg\'s book."')
print("Greg\'s book.")
#print('"Greg's book."') 
      #A linha 5 gerará SyntaxError, porque o símbolo ' no Greg's book. string requer um caractere de escape.
      
print(0x123)

print(0.0000000000000000000001)
#O Python sempre escolhe a forma mais econômica de apresentação do número, 
# e você deve levar isso em consideração ao criar literais.

print("Eu gosto \"Monty Python\"")
 
print('Eu gosto "Monty Python"')
#sem escape

print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)


#esse programa calcula o número de segundos em um dado número de horas
# esse programa foi escrito a dois dias atrás

a = 2 # número de horas
seconds = 3600 # número de segundos em uma hora

print("Horas: ", a) #imprimindo o número de horas
# print("Seconds in Hours: ", a * seconds) # imprimindo o número de segundos em uma dada hora

#aqui também devería escrever "Adeus", mas o programador não teve tempo de escrever código
#esse é o final do programa que computa o número de segundos em 3 horas
 
 
#  #Isso é
# uma multilinha
# Comente. #
 
# print("Olá!")

print("Conta-me qualquer coisa...")
anything = input()
print("Hum...", anything, "... Realmente?")

anything = input("Conta-me qualquer coisa...")
print("Hum...", anything, "...Realmente?")
 
anything = input("Digite um número: ")
something = anything ** 2.0
print(anything, "elevado a 2 é", something)

# #Já dissemos isso, mas deve ser afirmado de forma inequívoca mais uma vez: o resultado da função input() é uma string.

# Uma string contendo todos os caracteres que o usuário insere no teclado. Não é um inteiro ou um float.

# Isso significa que você não deve usá-lo como argumento de nenhuma operação aritmética, por exemplo, você não pode usar esses dados para elevá-los ao quadrado, dividi-los por qualquer coisa ou dividir qualquer coisa por eles.
 
 
anything = float(input("Digite um número: "))
something = anything ** 2.0
print(anything, "elevado a 2 é", something)



# a função int() usa um argumento (por exemplo, uma string: int(string)) e tenta convertê-lo em um número inteiro; se falhar, o programa inteiro também falhará (há uma solução para essa situação, mas mostraremos isso um pouco mais tarde);
# a função float() usa um argumento (por exemplo, uma string: float(string)) e tenta convertê-la em um flutuante (o resto é o mesmo).

 





# leg_a = float(input("Insira o comprimento da primeira perna: "))
# leg_b = float(input("Insira o comprimento da segunda perna: "))
# hypo = (leg_a**2 + leg_b**2) ** .5
# print("O comprimento da hipotenusa é", hypo)

fnam = input("Posso ter seu primeiro nome, por favor? ")
lnam = input("Posso ter seu sobrenome, por favor? ")
print("Obrigado!.")
print("\nSeu nome é " + fnam + " " + lnam + ".")

