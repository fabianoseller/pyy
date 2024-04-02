# Interseção de Conjuntos:
#Crie dois conjuntos com seus hobbies e os hobbies de um amigo.
#Encontre os hobbies em comum entre vocês e imprima-os.


# Verificação de Elemento
amigos = {"João", "Maria", "Ana", "Pedro"}  # Conjunto com os nomes dos seus amigos
nome = input("Digite o nome: ")
if nome in amigos:
    print(nome, "é seu amigo.")
else:
    print(nome, "não é seu amigo.")

# Interseção de Conjuntos
seus_hobbies = {"Leitura", "Caminhada", "Fotografia"}
hobbies_amigo = {"Leitura", "Cinema", "Fotografia"}
hobbies_em_comum = seus_hobbies.intersection(hobbies_amigo)
print("Hobbies em comum:", hobbies_em_comum)

# Interseção de Conjuntos
seus_hobbies = {"Leitura", "Caminhada", "Fotografia"}
hobbies_amigo = {"Leitura", "Cinema", "Fotografia"}
hobbies_em_comum = seus_hobbies.intersection(hobbies_amigo)
print("Hobbies em comum:", hobbies_em_comum)