# https://iaexpert.academy/2019/09/12/dicionarios-em-python/
#  Crie dois dicionários com as informações de dois alunos e compare seus 
# nomes e idades.
# • Crie dois dicionários com as informações de dois produtos e compare seus 
# preços.
# • Crie dois dicionários com as informações de dois livros e compare seus 
# autores.
# • Crie dois dicionários com as informações de dois filmes e compare seus 
# diretores.

aluno1 = {'nome': 'João', 'idade': 20}
aluno2 = {'nome': 'Maria', 'idade': 22}

# Comparando nomes e idades dos alunos
if aluno1['nome'] == aluno2['nome']:
    print("Os alunos têm o mesmo nome.")
else:
    print("Os alunos têm nomes diferentes.")

if aluno1['idade'] == aluno2['idade']:
    print("Os alunos têm a mesma idade.")
else:
    print("Os alunos têm idades diferentes.")

# Dicionários de produtos
produto1 = {'nome': 'Livro', 'preco': 10.50}
produto2 = {'nome': 'Caderno', 'preco': 12.50}

# Comparando preços dos produtos
if produto1['preco'] == produto2['preco']:
    print("Os produtos têm o mesmo preço.")
else:
    print("Os produtos têm preços diferentes.")

# Dicionários de livros
livro1 = {'titulo': 'Harry Potter', 'autor': 'J.K. Rowling'}
livro2 = {'titulo': 'Game of Thrones', 'autor': 'George R.R. Martin'}

# Comparando autores dos livros
if livro1['autor'] == livro2['autor']:
    print("Os livros têm o mesmo autor.")
else:
    print("Os livros têm autores diferentes.")

# Dicionários de filmes
filme1 = {'titulo': 'Titanic', 'diretor': 'James Cameron'}
filme2 = {'titulo': 'Inception', 'diretor': 'James Cameron'}

# Comparando diretores dos filmes
if filme1['diretor'] == filme2['diretor']:
    print("Os filmes têm o mesmo diretor.")
else:
    print("Os filmes têm diretores diferentes.")