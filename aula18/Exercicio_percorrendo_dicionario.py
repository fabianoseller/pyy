amigo = {
    "nome": "Carlos",
    "idade": 30,
    "profissao": "Engenheiro",
    "cidade": "São Paulo"
}

# Imprimindo cada chave e valor em linhas separadas:
for chave, valor in amigo.items():
    print(f"{chave}: {valor}")

print()  # Linha em branco para separar

#Dicionário de Produto**:
produto = {
    "nome": "Smartphone",
    "preco": 899.99,
    "cor": "Preto",
    "tamanho": "Médio"
}

# Imprimindo todos os valores em uma única linha:
print(f"Produto: {produto['nome']}, Preço: ${produto['preco']:.2f}, Cor: {produto['cor']}, Tamanho: {produto['tamanho']}")

print()  # Linha em branco para separar

# Dicionário de Livro

livro = {
    "titulo": "Dom Casmurro",
    "autor": "Machado de Assis",
    "ano_publicacao": 1899,
    "genero": "Romance"
}

# Imprimindo as chaves "título" e "autor" em uma única linha:

print(f"Livro: {livro['titulo']} (Autor: {livro['autor']})")

print()  # Linha em branco para separar

# Dicionário de Filme 

filme = {
    "nome": "Matrix",
    "diretor": "Lana Wachowski",
    "ano_lancamento": 1999,
    "genero": "Ficção Científica"
}

# Imprimindo as chaves "nome" e "diretor" em uma única linha:
print(f"Filme: {filme['nome']} (Diretor: {filme['diretor']})")