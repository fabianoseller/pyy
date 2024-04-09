# #Criando e acessando dicionários:

# Crie um dicionário para armazenar informações sobre um filme, incluindo 
# título, ano, diretor e atores principais.
# Acesse o ano de lançamento do filme usando a chave apropriada.
# Modifique o valor do diretor para um novo diretor.
# Adicione uma nova chave-valor ao dicionário para incluir a duração do 
# filme.

# Criando o dicionário com informações sobre o filme brasileiro
# Criando o dicionário com informações sobre o filme brasileiro
filme_brasileiro = {
    "título": "Cidade de Deus",
    "ano": 2002,
    "diretor": "Fernando Meirelles",
    "atores_principais": ["Alexandre Rodrigues", "Leandro Firmino", "Matheus Nachtergaele"],
}

# Exibindo as informações sobre o filme antes das atualizações
print("Informações sobre o filme brasileiro (antes da atualização):")
print(filme_brasileiro)

# Modificando o valor do diretor para um novo diretor
novo_diretor = "Kátia Lund"
filme_brasileiro["diretor"] = novo_diretor

# Adicionando uma nova chave-valor para incluir a duração do filme
filme_brasileiro["duração"] = "130 minutos"

# Exibindo o dicionário atualizado
print("\nInformações sobre o filme brasileiro (após as atualizações):")
print(filme_brasileiro)

print(f"\nO diretor foi atualizado para: {filme_brasileiro['diretor']}")

    
    
    
    ####  
    
#     # Criando o dicionário com informações sobre o filme brasileiro
# filme_brasileiro = {
#     "título": "Cidade de Deus",
#     "ano": 2002,
#     "diretor": "Fernando Meirelles",
#     "atores_principais": ["Alexandre Rodrigues", "Leandro Firmino", "Matheus Nachtergaele"],
# }

# # Acessando o ano de lançamento do filme
# ano_lancamento = filme_brasileiro["ano"]
# print("Ano de lançamento:", ano_lancamento)

# # Modificando o valor do diretor para um novo diretor
# novo_diretor = "Kátia Lund"
# filme_brasileiro["diretor"] = novo_diretor
# print("Diretor atualizado:", filme_brasileiro["diretor"])

# # Adicionando uma nova chave-valor para incluir a duração do filme
# filme_brasileiro["duração"] = "130 minutos"

# # Exibindo o dicionário atualizado
# print("\nDicionário de informações sobre o filme brasileiro:")
# for chave, valor in filme_brasileiro.items():
#     print(f"{chave.capitalize()}: {valor}")

