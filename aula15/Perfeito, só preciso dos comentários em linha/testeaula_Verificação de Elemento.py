# 7. Remoção de elementos duplicados
conjunto = {'Maria', 'Joana', 'Dionisio', 'Alana'}
sem_duplicados = set()
for elemento in conjunto:
 
 
    sem_duplicados.add(elemento)

print("Conjunto sem elementos duplicados:", sem_duplicados)
if conjunto != []:
      print("Lista de  nomes no conjunto:", conjunto)
else:
      print("Sua lista está vazia")

novo_nome = input("Escreva o novo nome do da pessoa a ser considerada na lista amigo(a):   ")

print('O novonome da pesoa é:', novo_nome)
while True:
    if  novo_nome in conjunto:
         print("O nome inserido pertence a lista de amigos conhecidos. ")
         break
   
    else: 
        print("O nome não pertence a lista de amigos já listados, ou seja, não é uma pessoa 'amiga' kkk.")
        break
        


#1. Verificação de Elemento:
#Crie um conjunto com os nomes de seus amigos.
#Peça ao usuário para digitar um nome.
#Verifique se o nome está no conjunto e informe o usuário se ele é seu amigo ou não.