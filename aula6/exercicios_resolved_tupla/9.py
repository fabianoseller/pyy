tupla_impares = tuple(range(1, 11, 2))
#Esta linha cria uma tupla chamada tupla_impares usando a função tuple().
#A função tuple() recebe um objeto iterável como argumento e retorna uma tupla contendo os elementos do objeto iterável.
#Neste caso, o objeto iterável é a função range(1, 11, 2).
#A função range() gera uma sequência de números começando em 1 e terminando em 9 (sem incluir o 11), com um passo de 2.
#Ou seja, a sequência gerada pela função range() é: [1, 3, 5, 7, 9].
#A função tuple() converte essa sequência em uma tupla, que é atribuída à variável tupla_impares.')
print(f"Tupla com valores ímpares de 1 a 10: {tupla_impares}")
