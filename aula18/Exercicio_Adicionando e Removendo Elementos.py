produto = {
    "nome": "Smartphone",
    "preco": 899.99,
    "cor": "Preto",
    "tamanho": "Médio"
}
print(f"Dicionário de Produto (COM a chave 'cor'): {produto}")
# Removendo a chave "cor"
del produto["cor"]

print(f"Dicionário de Produto (sem a chave 'cor'): {produto}")

livro = {
    "titulo": "Dom Casmurro",
    "autor": "Machado de Assis",
    "ano_publicacao": 1899,
    "genero": "Romance"
}
# Adicionando a chave "tradução"
print(f"Dicionário de Livro (SEM a chave 'tradução'): {livro}")

# Adicionando a chave "tradução"
livro["traducao"] = "Sim"

print(f"Dicionário de Livro (com a chave 'tradução'): {livro}")