
# 2. Interseção de conjuntos: Escreva um programa que encontre a interseção de dois conjuntos. Utilize for para iterar pelos 
# elementos e if para verificar a presença em ambos os conjuntos

conjunto_element={'do', 're', 'mi', 'si'}
conjunto_element2={'fa', 'so', 'la', 'si'}
conjunto_comum=set()
if conjunto_element != conjunto_element2:
    conjunto_comum = conjunto_element & conjunto_element2
    print(f'{conjunto_comum}')
else:
    print(f'Não contém.')
    
    #3. Escreva um programa que encontre a diferença entre dois conjuntos. Utilize for para iterar pelos 
# elementos e if para verificar a presença no primeiro conjunto e não no segundo.

conjunto_element1={1,6,8, 10, 5}
conjunto_element2={6, 7, 8, 9, 10}

conjunto_diferente=set()

conjunto_diferente = conjunto_element1.symmetric_difference(conjunto_element2)
if conjunto_diferente != set():
    print(f'{conjunto_diferente}')
else:
    print('Não há diferenças!')
    
    
 #diff conjuntos
livros_lidos = {"Dom Quixote", "Orgulho e Preconceito", "O Grande Gatsby", "Cem Anos de Solidão"}
livros_desejados = {"1984", "O Senhor dos Anéis", "Crime e Castigo", "O Pequeno Príncipe"}

livros_nao_lidos = set()

for livro in livros_desejados:
    if livro not in livros_lidos:
        livros_nao_lidos.add(livro)

print("Livros que você ainda não leu:")
for livro in livros_nao_lidos:
    print(livro)
    
    #subconjuntos
    paises_america_sul = {"Brasil", "Argentina", "Chile", "Colômbia", "Peru"}
paises_visitados = {"Brasil", "Argentina"}

if paises_visitados.issubset(paises_america_sul):
    print("Você visitou todos os países da América do Sul!")
else:
    print("Há países da América do Sul que você ainda não visitou.")
    
    #ordenação elemtos
numeros = {5, 9, 2, 7, 1, 8, 3, 10, 6, 4}

# Ordenação crescente
ordenado_crescente = []
for i in range(1, max(numeros)+1):
    if i in numeros:
        ordenado_crescente.append(i)







