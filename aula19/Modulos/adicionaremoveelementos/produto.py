# produto.py
produto = {
    "nome": "Smartphone",
    "preco": 899.99,
    "cor": "Preto",
    "tamanho": "Médio"
}

def remover_cor(produto):
    del produto["cor"]
    return produto


