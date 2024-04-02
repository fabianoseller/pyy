#Crie um conjunto com os livros que você já leu e outro com os livros que você deseja ler.
#Encontre os livros que você ainda não leu e imprima a lista.
# Diferença de Conjuntos
livros_lidos = {"Dom Casmurro", "O Pequeno Príncipe", "1984"}
livros_desejados = {"Harry Potter", "A Revolução dos Bichos", "O Senhor dos Anéis", "1984"}
livros_nao_lidos = livros_desejados - livros_lidos
print("Livros que você ainda não leu:", livros_nao_lidos)
