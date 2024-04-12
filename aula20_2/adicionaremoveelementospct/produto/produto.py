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