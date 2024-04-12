
# livro.py
livro = {
    "titulo": "Dom Casmurro",
    "autor": "Machado de Assis",
    "ano_publicacao": 1899,
    "genero": "Romance"
}

def adicionar_traducao(livro):
    livro["traducao"] = "Sim"
    return livro