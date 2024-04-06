
# Criando um dicionário vazio
pessoa = {}

# Adicionando as chaves "nome" e "idade"
pessoa["nome"] = "Maria"
pessoa["idade"] = 25
pessoa["Genero"] = "Não binario"

print(f"Dicionário de Pessoa: {pessoa}")



#Crie um dicionário com as informações de um produto e remova a chave 
"cor"

produto = {
    "nome": "Smartphone",
    "preco": 899.99,
    "cor": "Preto",
    "tamanho": "Médio"
}
#com chae cor

print(f"Dicionário de Produto (COM a chave 'cor'): {produto}")
# Removendo a chave "cor"
del produto["cor"]

print(f"Dicionário de Produto (sem a chave 'cor'): {produto}")



#Dicionário de Livro com Adição da Chave “tradução”:
livro = {
    "titulo": "Dom Casmurro",
    "autor": "Machado de Assis",
    "ano_publicacao": 1899,
    "genero": "Romance"
}

# Adicionando a chave "tradução"
livro = {
    "titulo": "Dom Casmurro",
    "autor": "Machado de Assis",
    "ano_publicacao": 1899,
    "genero": "Romance"
}

# Adicionando a chave "tradução"
livro["traducao"] = "Sim"

print(f"Dicionário de Livro (com a chave 'tradução'): {livro}")


#Dicionário de Filme com Remoção da Chave “ano de lançamento”:

filme = {
    "nome": "Matrix",
    "diretor": "Lana Wachowski",
    "ano_lancamento": 1999,
    "genero": "Ficção Científica"
}

# Removendo a chave "ano de lançamento"
filme.pop("ano_lancamento", None)  # O segundo argumento evita erro se a chave não existir

print(f"Dicionário de Filme (sem a chave 'ano de lançamento'): {filme}")