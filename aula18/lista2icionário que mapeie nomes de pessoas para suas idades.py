# 2. Criar um dicionário que mapeie nomes de pessoas para suas idades
pessoas_idades = {
    "João": 30,
    "Maria": 25,
    "Pedro": 40,
    "Ana": 35
}

# Iterar sobre o dicionário e imprimir as pessoas e suas idades
print("Pessoas e suas idades:")
for pessoa, idade in pessoas_idades.items():
    print(f"{pessoa}: {idade} anos")

# Atualizar a idade de uma pessoa
nome = input("Digite o nome da pessoa que deseja atualizar a idade: ")
nova_idade = int(input("Digite a nova idade: "))

# Garantir que a nova idade seja diferente da idade anterior
while nova_idade == pessoas_idades.get(nome):
    print("A nova idade não pode ser igual à idade anterior.")
    nova_idade = int(input("Digite uma nova idade diferente: "))

pessoas_idades[nome] = nova_idade

# Imprimir o dicionário atualizado
print("\nPessoas e suas novas idades:")
for pessoa, idade in pessoas_idades.items():
    print(f"{pessoa}: {idade} anos")
