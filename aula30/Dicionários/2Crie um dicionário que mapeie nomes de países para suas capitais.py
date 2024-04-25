# Criando o dicionário de países e suas capitais
paises = {
    "Brasil": "Brasília",
    "Argentina": "Buenos Aires",
    "Portugal": "Lisboa",
    "França": "Paris",
    "Espanha": "Madri",
}

# Definindo o país a ser pesquisado
pais = "Alemanha"

# Buscando a capital usando o método get()
capital = paises.get(pais)

# Tratando o caso de chave inexistente
if capital is None:
    # Imprimindo uma mensagem informativa
    print(f"A capital do país '{pais}' não está no dicionário.")
else:
    # Imprimindo a capital do país
    print(f"A capital do país '{pais}' é '{capital}'.")