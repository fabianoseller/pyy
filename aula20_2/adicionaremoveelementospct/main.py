# #meu_pacote/
# │
# ├── __init__.py
# │
# ├── produto/
# │   ├── __init__.py
# │   └── produto.py
# │
# └── livro/
#     ├── __init__.py
#     └── livro.py


import livro.livro as liv
import produto.produto as prod
produto_sem_cor = prod.remover_cor(prod.produto)


produto_sem_cor = prod.remover_cor(prod.produto)



livro_com_traducao = liv.adicionar_traducao(liv.livro)
print(f"Dicionário de Livro (com a chave 'tradução'): {livro_com_traducao}")

