#Crie um dicionário que mapeie números de telefone para nomes de pessoas.
# Utilize o método pop() para remover
# um número de telefone do dicionário e, em seguida, 
# verifique se a chave foi removida.



# 4. Criar um dicionário que mapeie números de telefone para nomes de pessoas
telefones_pessoas = {
    "123456789": "João",
    "987654321": "Maria",
    "456789123": "Pedro",
    "321654987": "Ana"
}

# Utilizar o método pop() para remover um número de telefone do dicionário e verificar se a chave foi removida
telefone = "123456789"
pessoa_removida = telefones_pessoas.pop(telefone, None)
if pessoa_removida is not None:
    print(f"O número de telefone {telefone} foi removido, correspondendo a {pessoa_removida}")
else:
    print(f"O número de telefone {telefone} não foi encontrado")

print(telefones_pessoas)  # Verificar se a chave foi removida
