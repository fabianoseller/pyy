operacao_listas = "04"
if operacao_listas == "04":
    print("################################## Modificação ##################################")
    print("Você pode modificar elementos da lista usando o operador de atribuição =.")
    lista_nomes = ["Lucas", "Rodolfo", "Aristeu"]
    try:
        # Modificando um elemento da lista usando o operador de atribuição =
        print("# Modificando um elemento da lista usando o operador de atribuição =: lista_nomes[1] = 'Teles'")
        lista_nomes[1] = 'Teles'
        # Imprimindo a lista atualizada
        print("Imprimindo a lista atualizada:", lista_nomes)  # Saída: ['Lucas', 'Teles', 'Aristeu']
    except Exception as e:
        print("Ocorreu um erro durante a operação:", e)
elif operacao_listas == "05":
    print("Você pode converter uma lista em uma string usando a função str().")
    minha_lista = [1, 2, 3]
    try:
        # Convertendo uma lista em uma string usando a função str()
        print("Exemplo: minha_string = str(minha_lista)")
        minha_string = str(minha_lista)
        print(f"Retorna: {minha_string}")
        tipo = type(minha_string)
        print(f"Tipo: {tipo}")
    except Exception as e:
        print("Ocorreu um erro durante a operação:", e)
elif operacao_listas == "06":
    print("Você pode converter uma lista em uma tupla usando o construtor tuple().")
    minha_lista = [1, 2, 3]
    try:
        # Convertendo uma lista em uma tupla usando o construtor tuple()
        print("Exemplo: minha_tupla = tuple(minha_lista)")
        minha_tupla = tuple(minha_lista)
        print(f"Retorna: {minha_tupla}")
    except Exception as e:
        print("Ocorreu um erro durante a operação:", e)
elif operacao_listas == "07":
    print("################################## Concatenar listas ##################################")
    print("O operador + pode ser usado para concatenar duas listas, criando uma nova lista com os elementos das duas listas originais.")
    minha_lista_string = ["a", "b", "c"]
    lista_nomes = ["Lucas", "Rodolfo", "Aristeu"]
    try:
        # Concatenando listas usando o operador +
        print("lista_concatenada = minha_lista_string + lista_nomes.")
        lista_concatenada = minha_lista_string + lista_nomes
        print(lista_concatenada)
    except Exception as e:
        print("Ocorreu um erro durante a operação:", e)
elif operacao_listas == "08":
    print("################################## Método extend() ##################################")
    print("O método extend() de uma lista pode ser usado para adicionar os elementos de outra lista à lista original.")
    lista_nomes = ["Lucas", "Rodolfo", "Aristeu"]
    minha_lista_int = [1, 2, 3]
    try:
        # Usando o método extend() para adicionar elementos de uma lista a outra
        print("lista_nomes.extend(minha_lista_int)")
        lista_nomes.extend(minha_lista_int)
        print(lista_nomes)
    except Exception as e:
        print("Ocorreu um erro durante a operação:", e)
elif operacao_listas == "09":
    print("################################## Função zip() ##################################")
    print("A função zip() pode ser usada para criar uma lista de tuplas, onde cada tupla contém os elementos da mesma posição nas listas originais.")
    lista_nomes = ["Lucas", "Rodolfo", "Aristeu"]
    try:
        # Usando a função zip() para criar uma lista de tuplas
        print("lista_conctenada = list(zip(lista_nomes, lista_nomes))")
        lista_conctenada = list(zip(lista_nomes, lista_nomes))
        print(lista_conctenada)
    except Exception as e:
        print("Ocorreu um erro durante a operação:", e)


operacao_listas = "01"
if operacao_listas == "01":
    print("################################## Adição ##################################")
    print("Você pode adicionar elementos ao final da lista usando o método append() ou inserir elementos em qualquer posição usando o método insert().")
    lista_nomes = ["Lucas", "Rodolfo", "Aristeu"]
    try:
        # Adicionando um elemento ao final da lista usando o método append()
        print("Adicionando um elemento ao final da lista usando o método append(): lista.append('Tiburcio')")
        lista_nomes.append('Tiburcio')
        # Imprimindo a lista atualizada
        print("Imprimindo a lista atualizada: ", lista_nomes)
        
        # Inserindo um elemento em uma posição específica usando o método insert()
        print("Inserindo um elemento em uma posição específica usando o método insert(): lista.insert(1, 'Edesvom')")
        lista_nomes.insert(1, 'Edesvom')
        # Imprimindo a lista atualizada
        print("Imprimindo a lista atualizada: ", lista_nomes)
        
    except Exception as e:
        print("Ocorreu um erro durante a operação:", e)
        
        
        
       # ---------------------------
       # 01 Encontrar o Maior Valor em uma Lista
lista = []
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

    lista.append(numero)
if lista != []:
    print("Lista de números inteiros:", lista)
else:
  print("Sua lista está vazia")
try:
    maior_valor = lista[0] # Define o maior valor como o primeiro elemento da lista.
    for i in range(1, len(lista)):# Itera pela lista a partir do segundo elemento
        if lista[i] > maior_valor:# Compara cada elemento com o maior valor atual
          maior_valor = lista[i]# Atualiza o maior valor se encontrar um elemento maior
    print(f"O maior valor é: {maior_valor}")# Exibe o maior valor encontrado
    #simplificação
    print(f"O maior valor é: {max(lista)}")
except ValueError:
  print("Para saber o maior valor, a lista deve ter pelo menos um elemento")
