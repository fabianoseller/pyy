#Crie um dicionário que mapeie nomes de países para suas capitais.
#Utilize o método get() para buscar a capital de um país específico,
#tratando o caso de chave inexistente.

# 1. Criar um dicionário que mapeie nomes de países para suas capitais
paises_capitais = {
    "Brasi": "Brasília",
    "Estados Unidos": "Washington",
    "França": "Paris",
    "Japão": "Tóquio"
}

# Utilizar o método get() para buscar a capital de um país específico
pais = "Brasil"
capital = paises_capitais.get(pais, "Capital não encontrada")
print(f"A capital do {pais} é {capital}")
