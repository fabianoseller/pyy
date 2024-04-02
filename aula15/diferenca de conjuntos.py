#Crie um conjunto com os livros que você já leu e outro com os livros que você deseja ler.
#Encontre os livros que você ainda não leu e imprima a lista.


livros_lidos = {'Dom Quixote', 'Cem Anos de Solidão', '1984', 'O Pequeno Príncipe'}
livros_desejados = {'Harry Potter', 'O Senhor dos Anéis', 'Crime e Castigo', 'O Código Da Vinci'}

livros_nao_lidos = livros_desejados - livros_lidos
print("Livros que ainda não li:", livros_nao_lidos)
