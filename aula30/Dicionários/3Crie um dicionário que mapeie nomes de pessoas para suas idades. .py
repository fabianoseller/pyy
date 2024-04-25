pessoas = {
    "João Silva": 25,
    "Maria Oliveira": 30,
    "Ana Souza": 22,
    "Pedro Santos": 35,
}

nome = "Ana Souza"

if nome in pessoas:
    # Pessoa está presente no dicionário
    idade = pessoas[nome]
    print(f"{nome} tem {idade} anos.")
else:
    # Pessoa não está presente no dicionário
    print(f"{nome} não está presente no dicionário.")