
import produto
import livro

print(f"Dicionário de Produto (COM a chave 'cor'): {produto.produto}")
produto_sem_cor = produto.remover_cor(produto.produto)
print(f"Dicionário de Produto (sem a chave 'cor'): {produto_sem_cor}")

print(f"Dicionário de Livro (SEM a chave 'tradução'): {livro.livro}")
livro_com_traducao = livro.adicionar_traducao(livro.livro)
print(f"Dicionário de Livro (com a chave 'tradução'): {livro_com_traducao}")
