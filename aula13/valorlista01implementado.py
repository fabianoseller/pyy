# 1. Encontrar o Maior Valor em uma Lista:
lista = [5, 3, 8, 1, 10]
maior_valor = max(lista)
print("O maior valor na lista é:", maior_valor)
print("********")


listerine = []
while True:
  tecla_parada = input("Pressione uma tecla para parar de agregar números à lista: ")
  if not tecla_parada.isdigit():#A função isdigit() verifica se a string digitada é composta apenas por dígitos. Se a string digitada for um número inteiro, uma mensagem de erro é exibida e o usuário é solicitado a digitar novamente.
    break
  else:
    print("Digite uma tecla, não um número.")

print("Sua tecla para parar é:", tecla_parada)
while True:
  
  valor = input("Digite um número inteiro e pressione enter para agregar o valor à lista (ou pressione {} para parar): ".format(tecla_parada))
  if valor == tecla_parada:
    break
  try:
    numero = int(valor)
  except ValueError:
    print("Valor inválido. Digite um número inteiro.")
  else:
   
    listerine.append(numero)
if listerine != []:
    print("listerine de números inteiros:", listerine)
else:
   print("Sua listerine está vazia")
try:
    maior_valor = listerine[0] # Define o maior valor como o primeiro elemento da listerine.
    for i in range(1, len(listerine)):# Itera pela listerine a partir do segundo elemento
        if listerine[i] > maior_valor:# Compara cada elemento com o maior valor atual
           maior_valor = listerine[i]# Atualiza o maior valor se encontrar um elemento maior
    print(f"O maior valor é: {maior_valor}")# Exibe o maior valor encontrado
    #simplificação
    print(f"O maior valor é: {max(listerine)}")
except ValueError:
  print("Para saber o maior valor, a listerine deve ter pelo menos um elemento")

  