produto = {
    "nome": "Smartphone",
    "preco": 899.99,
    "cor": "Preto",
    "tamanho": "Médio"
}



print(f"Dicionário de Produto (COM a chave 'cor'): {produto}\n")

# Removendo a chave "cor"
del produto["cor"]
# Dentro do módulo produto.produto

def remover_cor(produto):
    del produto["cor"]
    return produto


print(f"Dicionário de Produto (SEM a chave 'cor'): {produto}")

# produto/produto.py

produto = {
    "nome": "Smartphone",
    "preco": 899.99,
    "cor": "Preto",
    "tamanho": "Médio"
}


def remover_cor(produto):
    if "cor" in produto:
        del produto["cor"]
    return produto


