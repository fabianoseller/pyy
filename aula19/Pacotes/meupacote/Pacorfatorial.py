# # def fatorial(numero):
 
#                     print(f"Calculando fatorial({numero})...")
#                     if numero == 0:
#                         print(f"Fatorial({numero}) = 1")
#                         return 1
#                     else:
#                         resultado = numero * fatorial(numero - 1)
#                         print(f"Fatorial({numero}) = {numero} * fatorial({numero - 1})")
#                         print(f"Fatorial({numero - 1}) = {resultado}")
#                         return resultado

# numero_fatorial = 10

# resultado_fatorial = fatorial(numero_fatorial)

# print(f"Fatorial de {numero_fatorial}: {resultado_fatorial}")

# def calcular_fatorial(numero):
#     resultado = 1
#     for i in range(1, numero + 1):
#         resultado *= i
#     return resultado

#valor = int(input('Entre com um número para saber o fatorial:'))  
#fatorial = 1  
#while (valor > 1):  
#  fatorial = fatorial * valor  
#  valor = valor - 1  
#print('O fatorial é {}.'.format(fatorial))

def fatorial(n):                             #linha1
    print("Calculando o fatorial de %d" % n) #linha2
    if n==0 or n == 1:                       #linha3
        print("Fatorial de %d = 1" % n)      #linha4
        return 1                             #linha5
    else:                                    #linha6
        fat = n * fatorial(n-1)              #linha7
        print(" fatorial de %d = %d" % (n, fat) ) #linha8
    return fat                              #linha9

fatorial(4)