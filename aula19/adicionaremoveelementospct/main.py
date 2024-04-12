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


import adicionaremoveelementospct.produto as prod
import adicionaremoveelementospct.livro as liv 




print(f"Dicionário de Produto (COM a chave 'cor'): {prod.produto}")
produto_sem_cor = prod.remover_cor(prod.produto)
print(f"Dicionário de Produto (sem a chave 'cor'): {produto_sem_cor}")

print(f"Dicionário de Livro (SEM a chave 'tradução'): {liv.livro}")
livro_com_traducao = liv.adicionar_traducao(liv.livro)
print(f"Dicionário de Livro (com a chave 'tradução'): {livro_com_traducao}")

